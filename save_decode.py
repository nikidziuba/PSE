import hashlib
from Crypto.Cipher import AES
import os
import demjson3
import json

def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data.encode() + padding

def dump(file, data):
    with open(file, 'w') as f:
        f.write(str(data).replace('\'', '"').replace('True', 'true').replace('False', 'false'))




def encrypt(file, data):

    with open(file, 'rb') as f_og:
        with open(file + '.bak', 'wb') as f:
            f.write(f_og.read())


    data = str(data).replace('\'', '"').replace('True', 'true').replace('False', 'false')

    # Set the password
    password = b't36gref9u84y7f43g'

    # Generate a random IV
    iv = os.urandom(16)

    # Create a new AES cipher object
    key = hashlib.pbkdf2_hmac('sha1', password, iv, 100, 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the data
    encrypted_data = iv + cipher.encrypt(pad(data, AES.block_size))

    with open(file, 'wb') as f:
        f.write(encrypted_data)


def decrypt(file):
    with open(file, 'rb') as f:
        data = f.read()

    # Set the password
    password = b't36gref9u84y7f43g'

    # Extract the IV from the encrypted data
    iv = data[:16]

    # Create a new AES cipher object
    key = hashlib.pbkdf2_hmac('sha1', password, iv, 100, 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_data = cipher.decrypt(data[16:]).decode()


    while decrypted_data[-1] != '}':
        decrypted_data  = decrypted_data[:-1]

    return demjson3.decode(decrypted_data)
