"""imports"""
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Cipher:
    def __init__(self, password) -> None:
        self.key = Cipher.passwd_to_key(password)
        self.cipher = Fernet(self.key)

    @staticmethod
    def passwd_to_key(passwd) -> bytes:
        password = bytes(passwd, encoding='utf-8')
        __salt = b'\x82z\xaa}\xa5\x03\xd2\xf0\x05\xda\xfdc\xbd\xe4:\x13'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=__salt,
            iterations=480000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password))

    def encrypt_data(self, row_data):
        cipher_text = self.cipher.encrypt(row_data)
        return cipher_text

    def decrypt_data(self, ciphered_data):
        decrypted_data = self.cipher.decrypt(ciphered_data)
        return decrypted_data
