import json
import logging
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def settings(file: str) -> dict:
    """Loads a settings file into the program.
    Args:
        json_file (str): The path to the json file with the settings.
    Returns:
        dict: dictionary with settings
    """
    settings = None
    try:
        with open(file) as file:
            settings = json.load(file)
        logging.info("Settings loaded successfully")
    except OSError as err:
        logging.info("Settings not loaded")
        raise err
    return settings


def save_symmetric_key(key: bytes, file_name: str) -> None:
    """Saves a symmetric key to txt file.
    Args:
        key (bytes): Symmetric key.
        file_name (str): Name of txt file.
    """
    try:
        with open(file_name, "wb") as key_file:
            key_file.write(key)
        logging.info("Symmetric key saved")
    except OSError as err:
        logging.info("Symmetric key not saved")
        raise err
    

def load_symmetric_key(file_name: str) -> bytes:
    """Loads a symmetric key from txt file.
    Args:
        file_name (str): Name of txt file.
    Returns:
        bytes: Symmetric key for symmetric encoding algorithm.
    """
    try:
        with open(file_name, mode="rb") as key_file:
            key = key_file.read()
        logging.info("Symmetric key saved")
    except OSError as err:
        logging.info("Symmetric key not saved")
        raise err
    return key


def save_private_key(private_key, file_name: str) -> None:
    """Saves a private key to pem file.
    Args:
        private_key: Private key for asymmetric encoding algorithm.
        file_name (str): Pem file for private key.
    """
    try:
        with open(file_name, "wb") as private_out:
            private_out.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
        logging.info("Private key saved")
    except OSError as err:
        logging.info("Private key not saved")
        raise err
    

def load_private_key(private_pem: str):
    """Loads a private key from pem file.
    Args:
        private_pem (str): Name of pem file.
    Returns:
        Private key for asymmetric encoding algorithm.
    """
    private_key = None
    try:
        with open(private_pem, "rb") as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        logging.info("Private key loaded")
    except OSError as err:
        logging.info("Private key not loaded")
        raise err
    return private_key


def save_public_key(public_key, file_name: str) -> None:
    """Saves a public key to pem file.
    Args:
        public_key: Public key for asymmetric encoding algorithm.
        file_name (str): Pem file for public key.
    """
    try:
        with open(file_name, "wb") as public_out:
            public_out.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
        logging.info("Public key saved")
    except OSError as err:
        logging.info("Public key not saved")
        raise err
    

def load_public_key(public_pem: str):
    """Loads a public key from pem file.
    Args:
        public_pem (str): Name of pem file.
    Returns:
        Public key for asymmetric encoding algorithm.
    """
    public_key = None
    try:
        with open(public_pem, "rb") as pem_in:
            public_bytes = pem_in.read()
        public_key = load_pem_public_key(public_bytes)
        logging.info("Public key saved")
    except OSError as err:
        logging.info("Public key not saved")
        raise err
    return public_key


def read_text(file_name: str) -> bytes:
    """Reads text from txt file.
    Args:
        file_name (str): Name of txt file.
    Returns:
        bytes: Text in byte form.
    """
    try:
        with open(file_name, mode="rb") as text_file:
            text = text_file.read()
        logging.info("Text read successfully")
    except OSError as err:
        logging.info("Text not read")
        raise err
    return text


def write_text(text: bytes, file_name: str) -> None:
    """Writes text to txt file.
    Args:
        text (bytes): Text for writing.
        file_name (str): Name of txt file.
    """
    try:
        with open(file_name, mode="wb") as text_file:
            text_file.write(text)
        logging.info("Text written successfully")
    except OSError as err:
        logging.info("Text not written")
        raise err
