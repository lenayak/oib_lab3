from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization


def decrypt_key(symmetric_encrypt_key, private_key):             #расшифровка симметричного ключа
    print("Symmetric key decryption")
    with open(symmetric_encrypt_key, 'rb') as file:
        sym_encrypt_key = file.read()
        sym_key = private_key.decrypt(sym_encrypt_key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        return sym_key


def decrypt_text(sym_key, encrypted_file, decrypted_file):      #дешифрование текста
    with open(encrypted_file, 'rb') as enc_f, open(decrypted_file, 'w') as dec_f:
        iv = enc_f.read(8)
        cipher_text = enc_f.read()
        cipher = Cipher(algorithms.Blowfish(sym_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(cipher_text)+decryptor.finalize()
        unpadder = pd.ANSIX923(32).unpadder()
        unpadded_dc_text = unpadder.update(dc_text)+unpadder.finalize()
        print(unpadded_dc_text.decode('utf-8'))
        dec_f.write(unpadded_dc_text.decode('utf-8'))


def get_private_key(private_pem):          # чтение закрытого ключа 
    with open(private_pem, 'rb')as file:
        private_key = serialization.load_pem_private_key(file.read(), password = None)
        return private_key
