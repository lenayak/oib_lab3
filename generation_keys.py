import os
import json

import cryptography

import info


def gen_key_for_sym():
    key = os.urandom(32) # это байты
    print(type(key))
    print(key)
    return key


def encrypt_key(key):
    cipher = cryptography.hazmat.primitivities.ciphers.algorithms.Blowfish(key)
    # ???


def key_to_file(file_name, key):
    with open(file_name, 'wb') as file:
        file.write(key)


def key_from_file(file_name):
    with open(file_name, 'rb') as file:
        content = file.read()
    print(type(content))
    print(content)


# 8 вариант
# Blowfish, длина ключа от 32 до 448 бит с шагом 8 бит - предусмотреть
# пользовательский выбор длины ключа;

# 1. Генерация ключей гибридной системы

# Входные параметры:
# 1) путь, по которому сериализовать зашифрованный симметричный ключ;
# 2) путь, по которому сериализовать открытый ключ;
# 3) путь, по которому сериазизовать закрытый ключ.

# 1.1. Сгеренировать ключ для симметричного алгоритма.
# 1.2. Сгенерировать ключи для ассиметричного алгоритма.
# 1.3. Сериализовать ассиметричные ключи.
# 1.4. Зашифровать ключ симметричного шифрования открытым ключом и
#      сохранить по указанному пути 


