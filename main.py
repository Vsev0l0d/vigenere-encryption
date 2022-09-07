FIRST_SYMBOL = 'А'
LAST_SYMBOL = 'Я'
ALPHABET_LENGTH = ord(LAST_SYMBOL) - ord(FIRST_SYMBOL) + 1


def shift(symbol, number):
    if ord(symbol.upper()) + number < ord(FIRST_SYMBOL):
        return chr(ord(symbol) + number + ALPHABET_LENGTH)
    elif ord(symbol.upper()) + number > ord(LAST_SYMBOL):
        return chr(ord(symbol) + number - ALPHABET_LENGTH)

    return chr(ord(symbol) + number)


def encrypt(text, key, reverse=False):
    ciphertext = ''
    for i, symbol in enumerate(text):
        number = ord(key[i % len(key)].upper()) - ord(FIRST_SYMBOL)
        if reverse:
            number = -number
        ciphertext += shift(symbol, number)
    return ciphertext


def decrypt(ciphertext, key):
    return encrypt(ciphertext, key, True)


dd = encrypt("яяяЯЯЯ", "абв")
print(dd)
print(decrypt(dd, "абв"))
