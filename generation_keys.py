import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def gen_keys_for_asym():           #генерация пары ключей для асимметричного алгоритма шифрования
    print("Generating a key pair for an asymmetric encryption algorithm.\n")
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    return (private_key, public_key)


def gen_key_for_sym():              # генерация ключа симметричного аллгоритма шифрования
    print("Symmetric encryption algorithm key generation.")
    print("You can choose the key length yourself from 4 to 56 bytes\n (default 4 bytes)\n")
    size = 4
    input(size)
    key = os.urandom(size)        # от 4х до 56 байт 
    return key


def serializate(private_key, public_key,private_pem, public_pem):
    # сериализация открытого ключа в файл
    print("Serializing the public key to a file.")
    with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                 format=serialization.PublicFormat.SubjectPublicKeyInfo))
    # сериализация закрытого ключа в файл
    print("Serialization the private key to a file.")
    private_pem = 'private.pem'
    with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                  format=serialization.PrivateFormat.TraditionalOpenSSL,
                  encryption_algorithm=serialization.NoEncryption()))


def encrypt_key(public_key, key):     # шифрование ключа симметричного алгоритма
    print("Symmetric algorithm key encryption.")
    cipherkey = public_key.encrypt(key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label = None))
    return cipherkey


def key_to_file(file_name, key):                # сериализация ключа симмеричного алгоритма в файл
    with open(file_name, 'wb') as file:
        file.write(key)
