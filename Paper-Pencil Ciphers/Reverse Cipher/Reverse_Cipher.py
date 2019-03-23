message = input('What do you want to encrypt? ')

ciphertext = '' #ciphertext stored in this variable

i = len(message) - 1 #this is the index

while i>=0:
    ciphertext = ciphertext + message[i]
    i = i - 1
print('Your cipher text is: %s' % ciphertext)
