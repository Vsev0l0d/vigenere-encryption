import string
import sys

ALPHABET_LENGTH = 0x10FFFF + 1


def shift(symbol: string, number: int) -> string:
    if ord(symbol) + number >= ALPHABET_LENGTH:
        return chr(ord(symbol) + number - ALPHABET_LENGTH)
    elif ord(symbol) + number < 0:
        return chr(ord(symbol) + number + ALPHABET_LENGTH)
    return chr(ord(symbol) + number)


def encrypt(text: string, key: string, reverse: bool = False) -> string:
    ciphertext = ''
    for i, symbol in enumerate(text):
        number = ord(key[i % len(key)])
        if reverse:
            number = -number
        ciphertext += shift(symbol, number)
    return ciphertext


def decrypt(ciphertext: string, key: string) -> string:
    return encrypt(ciphertext, key, True)


FILENAME = sys.argv[1]
MODE = sys.argv[2]
with open(FILENAME, "r+", encoding="utf8") as file:
    text = file.read()
    keys = input("Введите составной ключ: ").split()
    for key in keys:
        if MODE.startswith("e"):
            text = encrypt(text, key)
        else:
            text = decrypt(text, key)

    file.seek(0)
    file.write(text)
