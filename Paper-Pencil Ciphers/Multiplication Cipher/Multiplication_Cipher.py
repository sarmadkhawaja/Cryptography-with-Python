alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def mult(shift, message):
    ciphertext = ''    
    for i in message:
        if i in alphabet:
            ciphertext = ciphertext + alphabet[(alphabet.index(i) * shift) % 26]
        elif i in ALPHABET:
            ciphertext = ciphertext + ALPHABET[(ALPHABET.index(i) * shift) % 26]
        else:
            ciphertext = ciphertext + i
        
    return ciphertext

print(mult(7, 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

