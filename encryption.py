from cryptography.fernet import Fernet

""""
#create key
key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key)
file.close()

"""

"""
#Decrypt the encrypted message
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)


"""


def encrypt(text, key_file):

    #Get the key from the file
    file  = open(str(key_file), 'rb')
    key=file.read()
    file.close()

    ##Encode the text
    encoded = text.encode()

    #Encrypt the message
    f = Fernet(key)
    encrypted = f.encrypt(encoded)

    #Decode the message
    value = encrypted.decode()

    return value

def decrypt(text, key):

    #Encode the text
    encoded=text.encode()

    #get the key from the key file
    file = open(str(key), 'rb')
    key = file.read()
    file.close()
    f2 = Fernet(key)
    decrypted=f2.decrypt(encoded)
    return decrypted


