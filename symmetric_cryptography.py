import os
import logging

from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def symmetric_decrypt(key: bytes, cipher_text: bytes) -> bytes:
    """Decrypts a symmetrical ciphertext using symmetric key.
    Args:
        key (bytes): Symmetric key of symmetric encryption algorithm.
        cipher_text (bytes): Encrypted text.
    Returns:
        bytes: Decrypted text.
    """
    cipher_text, iv = cipher_text[16:], cipher_text[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    text = decryptor.update(cipher_text) + decryptor.finalize()
    unpadder = pd.ANSIX923(64).unpadder()
    unpadded_text = unpadder.update(text) + unpadder.finalize()
    logging.info(
        "The symmetrical ciphertext using the symmetric key has been decrypted")
    return unpadded_text


def symmetric_encrypt(key: bytes, text: bytes) -> bytes:
    """Encrypts an input text using symmetric key.
    Args:
        key (bytes): Symmetric key of symmetric encryption algorithm.
        text (bytes): Text for encryption.
    Returns:
        bytes: Encrypted text.
    """
    padder = pd.ANSIX923(128).padder()
    padded_text = padder.update(text) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_text) + encryptor.finalize()
    logging.info("The text using the symmetric key has been encrypted")
    return iv + cipher_text