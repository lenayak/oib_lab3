import argparse

import generation_keys


parser = argparse.ArgumentParser()
parser.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
parser.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
parser.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
args = parser.parse_args()
if args.generation is not None:
    print('Generation keys')
elif args.encryption is not None:
    print('Encryption')
elif args.decryption is not None:
    print('Decryption')

