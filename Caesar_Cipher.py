plaintext = input('Please enter the text to encrypt: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar(shift):
    ciphertext = ''    
    for i in plaintext:
        if i in alphabet:
            ciphertext = ciphertext + alphabet[(alphabet.index(i) + shift) % 26]
        elif i in ALPHABET:
            ciphertext = ciphertext + ALPHABET[(ALPHABET.index(i) + shift) % 26]
        else:
            ciphertext = ciphertext + i
        
    return ciphertext

print(caesar(15))







        

