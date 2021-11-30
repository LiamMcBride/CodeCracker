import hashlib, binascii
import time

user_password = input("Please enter a password:\n")

start = time.time()

def hash(password):
    hashed_pwd = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), b'salt', 100000)
    return binascii.hexlify(hashed_pwd)

def read_dictionary(title):
    dict_array = []
    dict_file = open(title, "r")

    for line in dict_file:
        dict_array.append(line.rstrip("\n"))
    
    return (dict_array)

def crack_password(password, dictionary):
    for word in dictionary:
        if hash(word) == password:
            print(word + " is the correct password!")
            break

crack_password(hash(user_password), read_dictionary("small_list.txt"))

print(time.time() - start)


