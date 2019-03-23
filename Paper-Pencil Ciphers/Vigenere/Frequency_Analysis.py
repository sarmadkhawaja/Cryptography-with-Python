LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def getLetterCount(message):
#returns a dictionary (key,value) = (letter, how many times a letter appears in message)  

    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,\
        'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,'O': 0, 'P': 0,\
        'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0,\
        'Z': 0}

    for symbol in message.upper():
        if symbol in LETTERS:
            letterCount[symbol] += 1
    return letterCount

def getItemAtIndexZero(item):
    return item[0]

def getFrequencyOrder(message):
#returns a string of aphabet letters in the order of most frequently occuring in the message parameter
    
    #First, get a dicitonary of each letter and its frequency count in the message parameter
    letterToFreq = getLetterCount(message)
    
    #Second, get a dicitonary with (key,value) = (frequency, letter in the message with that frequency)
    freqToLetter = {}   
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    #Third, put each list of letters in reverse ETAOIN order and convert it to a string
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find,reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])
    
    #Fourth, convert freqToLetter to a list of tuples (key,value). Then sort this list in frequency order.
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    
    #Fifth, make a list of all the strings in freqPairs.
    freqOrder = []
    for pair in freqPairs:
        freqOrder.append(pair[1])
    return ''.join(freqOrder)

def EnglishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)
    matchScore = 0
    for common in freqOrder[:6]:
        if common in ETAOIN[:6]:
            matchScore += 1
    for uncommon in freqOrder[-6:]:
        if uncommon in ETAOIN[-6:]:
            matchScore += 1 
    return matchScore

print(EnglishFreqMatchScore('Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytrajp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcorl calrpx ypc lwjsxusx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqaxpx jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh.-Facjclxo Ctrramm'))




 