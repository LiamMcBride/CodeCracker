import hashlib, binascii
import time

'''
Backend portion of the project.
Authors: Liam McBride, Patrick Edmonds
Version: 12/01/2021
'''
class Cracker:
    def __init__(self, user_password, sha, dictionary):
        self.total = 0
        self.tested = 0
        self.currentPassword = None
        self.start = 0
        self.end = 0
        self.user_password = user_password
        self.solved = False
        self.failed = False
        self.sha = sha
        self.dictionary = dictionary
    
    def getCrackin(self):
        #Starts timer for the password cracking
        self.start = time.time()
        
        #This corrects for the difference in how eclipse, vs code, and command line treat the file systems.
        try:
            self.crack_password(hash(self.user_password), self.read_dictionary(self.dictionary))
        except:
            try:
                self.crack_password(hash(self.user_password), self.read_dictionary("./src/hw_13/" + self.dictionary))
            except:
                print("File system is not working. Please try via command line. See README.md for more info.")

    #Used to get final password for user display    
    def getCurrentPassword(self):
        return self.currentPassword

    #Used to get total time for user display
    def getTime(self):
        if(self.end - self.start < 0):
            return time.time() - self.start
        return self.end - self.start

    #Used to get total passwords tested for user display
    def getTotalDone(self):
        return self.tested

    #Hashes the password w/ either sha encrytion
    def hash(self, password):
        hashed_pwd = hashlib.pbkdf2_hmac(self.sha, password.encode('utf-8'), b'salt', 100000)
        return binascii.hexlify(hashed_pwd)

    #Reads the dictionary and gets rid of passwords that surpass the passwords length
    def read_dictionary(self, title):
        dict_array = []
        dict_file = open(title, "r", encoding="utf8")

        for line in dict_file:
            if len(self.user_password) >= len(line) - 1:
                dict_array.append(line.rstrip("\n"))
                self.total += 1
        
        if len(dict_array) == 0:
            print("No password in the dictionary matches this.")
            self.solved = True
        
        return (dict_array)

    #Tests the password against the dictionary    
    def crack_password(self, password, dictionary):
        #Tests single words from the dictionary
        for word in dictionary:
            self.currentPassword = word
            if len(self.user_password) == len(self.currentPassword):
                self.tested += 1
                print(self.currentPassword)
                if hash(word) == password:
                    self.end = time.time()
                    self.solved = True
                    print(word + " is the correct password!")
                    break
        if self.solved == False:
            #Tests passwords containing two words from the dictionary
            for word in dictionary:
                for word2 in dictionary:
                    self.currentPassword = word + word2
                    if len(self.user_password) == len(self.currentPassword):
                        
                        print(self.currentPassword)
                        self.tested += 1
                        if(hash(word + word2) == password):                        
                            self.end = time.time()
                            self.solved = True
                            print(word + word2 + " is the correct password!")
                            break
                if self.solved == True:
                    break

            if self.solved == False:
                #Tests passwords containing three words from the diction
                for word in dictionary:
                    for word2 in dictionary:
                        for word3 in dictionary:
                            self.currentPassword = word + word2 + word3
                            if len(self.user_password) == len(self.currentPassword):
                                
                                print(self.currentPassword)
                                self.tested += 1
                                if(hash(word + word2 + word3) == password):                        
                                    self.end = time.time()
                                    self.solved = True
                                    print(word + word2 + word3 + " is the correct password!")
                                    break

                        if self.solved == True:
                            break
                    
                    if self.solved == True:
                        break



                if self.solved == False:
                    self.failed = True