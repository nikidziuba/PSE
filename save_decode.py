import hashlib
from Crypto.Cipher import AES
import os

def pad(data, block_size):
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length)
    return data.encode() + padding


def encrypt(data):

    # Set the password
    password = b't36gref9u84y7f43g'

    # Generate a random IV
    iv = os.urandom(16)

    # Create a new AES cipher object
    key = hashlib.pbkdf2_hmac('sha1', password, iv, 100, 16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the data
    encrypted_data = iv + cipher.encrypt(pad(data, AES.block_size))


    return encrypted_data



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
    return decrypted_data

def find_str(text, find):

    str_index = text.index(find)

    ret_str = ''
    i = str_index + len(find)
    while text[i] != '}':
        ret_str += text[i]
        i += 1
    
    return ret_str

def change_str(text, find, change):
    start_index = text.index(find) + len(find)
    end_index = start_index
    while text[end_index] != '}':
        end_index += 1

    return text[:start_index] + str(change) + text[end_index:]

def get_info(file):
        data = decrypt(file)
        money_str = '"PlayersMoney":{"__type":"int","value":'
        player_money = find_str(data, money_str)

        level_str = '"Level":{"__type":"int","value":'
        player_level = find_str(data, level_str)

        return (player_money, player_level)

def change_info(file, money, level):

    data = decrypt(file)
    with open(file + '.bak', 'wb') as f:
        with open(file, 'rb') as og_f:
            f.write(og_f.read())

    money_str = '"PlayersMoney":{"__type":"int","value":'
    level_str = '"Level":{"__type":"int","value":'

    data = change_str(data, money_str, money)
    data = change_str(data, level_str, level)

    encrypted = encrypt(data)
    with open(file, 'wb') as f:
        f.write(encrypted)






