import hashlib, binascii
import time

class Cracker:
    def __init__(self, user_password):
        self.total = 0
        self.tested = 0
        self.currentPassword = None
        self.start = 0
        self.end = 0
        self.user_password = user_password
    
    def getCrackin(self):
        self.start = time.time()
        self.crack_password(hash(self.user_password), self.read_dictionary("src/hw_13/10k_list.txt"))
        
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
        dict_file = open(title, "r")

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
                print(word + " is the correct password!")
                break

# crack_password(hash(user_password), read_dictionary("small_list.txt"))

# print(time.time() - start)


