import os

# from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decrypt_key(symmetric_encrypt_key, private_key):             #расшифровка симметричного ключа
    print("Symmetric key decryption")
    with open(symmetric_encrypt_key, 'rb') as file:
        sym_encrypt_key = file.read()
        sym_key = private_key.decrypt(sym_encrypt_key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        return sym_key


def get_private_key(private_pem):          # чтение закрытого ключа 
    with open(private_pem, 'rb')as file:
        private_key = serialization.load_pem_private_key(file.read(), password = None)
        return private_key
    

def encrypt_text(initial_file_path, sym_key):               #шифрование текста симметричным алгоритмом
    print("Text encryption")
    with open(initial_file_path, 'rb') as file:
        text = file.read()
    iv = os.urandom(4)      #случайное значение для инициализации блочного режима, должно быть размером с блок и каждый раз новым
    cipher = Cipher(algorithms.Blowfish(sym_key), modes.CBC(iv))   #invlid iv for CBC
    encryptor = cipher.encryptor()     
    cipher_text = encryptor.update(text)+encryptor.finalize()    
    return cipher_text


def save_to_file(encrypted_file, cipher_text):        # сохранение зашифрованного текста в файл 
    with open(encrypted_file, 'wb') as file:
        file.write(cipher_text)