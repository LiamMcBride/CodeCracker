import hashlib, binascii
import time

'''
Backend portion of the project.
Authors: Liam McBride, Patrick Edmonds
Version: 12/01/2021
'''
class Cracker:
    def __init__(self, user_password, gui):
        self.total = 0
        self.tested = 0
        self.currentPassword = None
        self.start = 0
        self.end = 0
        self.user_password = user_password
        self.gui = gui
        self.solved = False
        self.failed = False
    
    def getCrackin(self):
        self.start = time.time()
        self.crack_password(hash(self.user_password), self.read_dictionary("src/hw_13/100k_list.txt"))
        
    def getTotalPasswords(self):
        return self.total
    
    def getCurrentPassword(self):
        return self.currentPassword

    def getTime(self):
        if(self.end - self.start < 0):
            return time.time() - self.start
        return self.end - self.start

    def getTotalDone(self):
        return self.tested

    def hash(self, password):
        hashed_pwd = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)
        return binascii.hexlify(hashed_pwd)

    def read_dictionary(self, title):
        dict_array = []
        dict_file = open(title, "r", encoding="utf8")

        for line in dict_file:
            dict_array.append(line.rstrip("\n"))
            self.total += 1
        
        return (dict_array)

    def crack_password(self, password, dictionary):
        for word in dictionary:
            self.currentPassword = word
            self.tested += 1
            print(self.currentPassword)
            if hash(word) == password:
                self.end = time.time()
                self.solved = True
                print(word + " is the correct password!")
                break
        if self.solved == False:
            self.failed = True




