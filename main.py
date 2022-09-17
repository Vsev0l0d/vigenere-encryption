import string

FIRST_SYMBOL = 'А'
LAST_SYMBOL = 'Я'
ALPHABET_LENGTH = ord(LAST_SYMBOL) - ord(FIRST_SYMBOL) + 1


def shift(symbol: string, number: int) -> string:
    if not (FIRST_SYMBOL <= symbol <= LAST_SYMBOL or FIRST_SYMBOL.lower() <= symbol <= LAST_SYMBOL.lower()):
        char = chr(ord(symbol) + number)
        while FIRST_SYMBOL <= char <= LAST_SYMBOL or FIRST_SYMBOL.lower() <= char <= LAST_SYMBOL.lower():
            char = chr(ord(char) + ALPHABET_LENGTH)
        return char

    if ord(symbol.upper()) + number < ord(FIRST_SYMBOL):
        return chr(ord(symbol) + number + ALPHABET_LENGTH)
    elif ord(symbol.upper()) + number > ord(LAST_SYMBOL):
        return chr(ord(symbol) + number - ALPHABET_LENGTH)

    return chr(ord(symbol) + number)


def encrypt(text: string, key: string, reverse: bool = False) -> string:
    ciphertext = ''
    for i, symbol in enumerate(text):
        number = ord(key[i % len(key)].upper()) - ord(FIRST_SYMBOL)
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

