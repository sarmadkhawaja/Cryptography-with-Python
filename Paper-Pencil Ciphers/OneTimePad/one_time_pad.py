import secrets

#we are using the key length and message length of 55 in the program

otp = ''
for i in range(55):
    otp += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

#The below code is exact same as the one for Vigenere cipher with the exception of key which is otp from above and message\
#for which the user is prompted to enter a plaintext/ciphertext with 55 letters

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def translate(message,mode):

    key = otp
    index = 0
    translated = ''

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if symbol.upper() in LETTERS:
            if mode == 'encrypt':
                num += LETTERS.find(key[index])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[index])
            num %= len(LETTERS)
            if symbol.isupper():
                translated += LETTERS[num]
            elif symbol.islower(): 
                translated += LETTERS[num].lower()
            index += 1
            index %= len(key)
        else:
            translated += symbol        
    return translated


#print(translate('IF YOU WANT TO SURVIVE OUT HERE, YOU’VE GOT TO KNOW WHERE YOUR TOWEL IS', 'encrypt'))