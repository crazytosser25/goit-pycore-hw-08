from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def password_to_key(passwd):
    return SHA256.new(passwd).digest()

password = input('Enter passwd: ')
key = password_to_key(password)
cipher = Fernet(key)
