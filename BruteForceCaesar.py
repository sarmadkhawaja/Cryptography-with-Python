letters = 'abcdefghijklmnopqrstuvwxyz'# lowercase alphabet containing the potential key
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # uppercase alphabet
 
def decrypt (message):    
    for key in letters:#test each key on encrypted message
        plaintext = ''
        ind = letters.index(key) #index of each potential key in the alphabet corresponds to number of positions shifted
        for symbol in message: 
            if symbol in letters: #symbol could be lower or upper case
                ind2 = letters.index(symbol) 
                PosShift = ind2 - ind #position of symbol after shift
                symbolPlaintext = letters[PosShift] #plaintext symbol
            elif symbol in LETTERS:
                ind2 = LETTERS.index(symbol) 
                PosShift = ind2 - ind #position of symbol after shift
                symbolPlaintext = LETTERS[PosShift] #plaintext symbol
            else:
                symbolPlaintext = symbol
            plaintext += symbolPlaintext
        print('Key = %s; Plaintext = %s\n' % (key,plaintext))
    return

print(decrypt('Adkt Ndj Vjnh! Cd WDBD!'))





