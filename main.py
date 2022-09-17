import string

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


text = "Реализовать шифрование и дешифрацию файла по методу Виженера с составным ключом."
keys = "итмо крутой университет".split()
print("текст: " + text)

for key in keys:
    text = encrypt(text, key)
print("зашифрованный текст: " + text)

for key in keys:
    text = decrypt(text, key)
print("расшифрованный текст: " + text)

