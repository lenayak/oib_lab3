import argparse
import logging
from load_info import settings
from generation_keys import create_keys
from encryption import encryption_text
from decryption import decryption_text

if __name__ == "__main__":
    info = settings("info.json")
    parser = argparse.ArgumentParser(description="Cryptosystem")
    parser.add_argument("-gen", "--generation", type = int, help="Запускает режим генерации ключей")
    parser.add_argument("-enc", "--encryption", action='store_true', help="Запускает режим шифрования")
    parser.add_argument("-dec", "--decryption", action='store_true', help="Запускает режим дешифрования")
    args = parser.parse_args()
    if args.generation:
        try:
            create_keys(args.generation, info)
            logging.info("Keys generation completed")
        except ValueError:
            logging.info(
                "Invalid key length: the key length should be from 40 to 128 in 8-bit increments."
            )
    elif args.encryption:
        try:
            encryption_text(info)
            logging.info("Encryption completed")
        except Exception:
            logging.info("Something is wrong with the encryption key")
    elif args.decryption:
        try:
            decryption_text(info)
            logging.info("Decryption completed")
        except Exception:
            logging.info("Something is wrong with the decryption key")