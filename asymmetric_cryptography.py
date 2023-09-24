import logging

from cryptography.hazmat.primitives.asymmetric import padding as pd
from cryptography.hazmat.primitives import hashes


def asymmetric_decrypt(private_key, cipher_text: bytes) -> bytes:
    """Decrypts an asymmetrical ciphertext using private key.
    Args:
        private_key: Private key of asymmetric encryption algorithm.
        cipher_text (bytes): Encrypted text.
    Returns:
        bytes: Decrypted text.
    """
    text = private_key.decrypt(
        cipher_text,
        pd.OAEP(
            mgf=pd.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    logging.info(
        "The asymmetric encrypted text using the private key has been decrypted")
    return text


def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    """Encrypts an input text using public key.
    Args:
        public_key: Public key of asymmetric encryption algorithm.
        text (bytes): Text for encryption.
    Returns:
        bytes: Encrypted text.
    """
    cipher_text = public_key.encrypt(
        text,
        pd.OAEP(
            mgf=pd.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    logging.info("The text using the public key has been encrypted")
    return cipher_text
