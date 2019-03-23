LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def translate(message,mode):

    mykey = input('Please enter your key: ')
    key = mykey.upper()
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

print (translate('Alan Mathison Turing was a British mathematician,logician, cryptanalyst, and computer scientist.', 'encrypt'))

        




   


    



