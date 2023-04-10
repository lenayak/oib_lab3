import argparse

import generation_keys, encryption, decryption
from info import *


parser = argparse.ArgumentParser()
parser.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
parser.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
parser.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
args = parser.parse_args()
if args.generation is not None:
    print('Generation keys\n')
    sym_key = generation_keys.gen_key_for_sym()
    keys = generation_keys.gen_keys_for_asym()
    private_key = keys[0]
    public_key = keys[1]
    generation_keys.serializate(private_key, public_key, private_pem, public_pem)
    cipher_key = generation_keys.encrypt_key(public_key, sym_key)
    generation_keys.key_to_file(symmetric_encrypt_key, cipher_key)
elif args.encryption is not None:
    print('Encryption\n')
    private_key = encryption.get_private_key(private_pem)
    sym_key = encryption.decrypt_key(symmetric_encrypt_key, private_key)
    cipher_text = encryption.encrypt_text(initial_file_path, sym_key)
    encryption.save_to_file(encrypted_file, cipher_text)
elif args.decryption is not None:
    print('Decryption\n')
    private_key = decryption.get_private_key(private_pem)
    sym_key = decryption.decrypt_key(symmetric_encrypt_key, private_key)
    cipher_text = decryption.decrypt_text(sym_key, encrypted_file, decrypted_file)
