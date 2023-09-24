import logging

from load_info import load_private_key, load_symmetric_key, read_text,write_text
from asymmetric_cryptography import asymmetric_decrypt
from symmetric_cryptography import symmetric_decrypt, symmetric_encrypt


def encryption_text(settings: dict) -> None:
    """Reads the saves keys and encrypts the specified text, writing it to a new text file.
    Args:
        settings (dict): Dictionary with paths.
    """
    private_key = load_private_key(settings["private"])
    cipher_key = load_symmetric_key(settings["symmetric_key"])
    symmetric_key = asymmetric_decrypt(private_key, cipher_key)
    text = read_text(settings["initial_file"])
    cipher_text = symmetric_encrypt(symmetric_key, text)
    write_text(cipher_text, settings["encrypted_file"])
    logging.info("The text using the keys has been encrypted")


def decryption_text(settings: dict) -> None:
    """Reads an encrypts text file and decrypts the text using keys, saving it to a new file.
    Args:
        settings (dict): Dictionary with paths.
    """
    cipher_text = read_text(settings["encrypted_file"])
    private_key = load_private_key(settings["private"])
    cipher_key = load_symmetric_key(settings["symmetric_key"])
    symmetric_key = asymmetric_decrypt(private_key, cipher_key)
    text = symmetric_decrypt(symmetric_key, cipher_text)
    write_text(text, settings["decrypted_file"])
    logging.info("The text was decrypted and written to a file") 
       