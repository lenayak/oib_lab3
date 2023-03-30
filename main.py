import argparse

import generation_keys
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
    cipher = generation_keys.encrypt_key(public_key, sym_key)
    generation_keys.key_to_file(symmetric_encrypt_key, cipher)
elif args.encryption is not None:
    print('Encryption\n')
elif args.decryption is not None:
    print('Decryption\n')

