"""imports"""
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Cipher:
    """A class to handle encryption and decryption
    using a password-based key derivation function.

    Attributes:
        key (bytes): The derived key from the given password.
        cipher (Fernet): The Fernet cipher object initialized with
            the derived key.

    Methods:
        encrypt_data(row_data: bytes) -> bytes:
            Encrypts the provided data and returns the encrypted data.
        
        decrypt_data(ciphered_data: bytes) -> bytes:
            Decrypts the provided encrypted data and returns the original data.
    """
    def __init__(self, password: str) -> None:
        self.key = Cipher.__passwd_to_key(password)
        self.cipher = Fernet(self.key)

    @staticmethod
    def __passwd_to_key(passwd: str) -> bytes:
        """Derives a key from the provided password using PBKDF2HMAC.

        Args:
            passwd (str): The password to derive the encryption key.

        Returns:
            bytes: The derived key encoded in a URL-safe base64 format.
        """
        password = bytes(passwd, encoding='utf-8')
        __salt = b'\x82z\xaa}\xa5\x03\xd2\xf0\x05\xda\xfdc\xbd\xe4:\x13'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=__salt,
            iterations=480000,
        )
        return base64.urlsafe_b64encode(kdf.derive(password))

    def encrypt_data(self, row_data: bytes) -> bytes:
        """Encrypts the provided data using the derived key.

        Args:
            row_data (bytes): The data to be encrypted.

        Returns:
            bytes: The encrypted data.
        """
        cipher_text = self.cipher.encrypt(row_data)
        return cipher_text

    def decrypt_data(self, ciphered_data: bytes) -> bytes:
        """Decrypts the provided encrypted data using the derived key.

        Args:
            ciphered_data (bytes): The encrypted data to be decrypted.

        Returns:
            bytes: The original decrypted data.
        """
        decrypted_data = self.cipher.decrypt(ciphered_data)
        return decrypted_data
