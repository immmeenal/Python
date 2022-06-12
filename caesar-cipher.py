import string

plain_text = "hello world"
shift = 3
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)

cipher_text = "khoor zruog"
shift = 26-3
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

decrypted = cipher_text.translate(table)

print(decrypted)