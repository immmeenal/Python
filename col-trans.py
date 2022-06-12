plaintext = "hello world"
key = 3

ciphertext = [''] * key

for column in range(key):
    pointer = column

    while pointer < len(plaintext):
        ciphertext[column] += plaintext[pointer]
        print(ciphertext)
        pointer += key

print(''.join(ciphertext))