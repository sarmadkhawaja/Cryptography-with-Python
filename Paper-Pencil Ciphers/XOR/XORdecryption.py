import base64
from itertools import cycle
def xor_decrypt(ciphertext, key):
    ciphertext_ascii = base64.decodestring(ciphertext)
    xor_tuples_list = list(zip(ciphertext_ascii,cycle(key))) #each tuple in the list contains ith symbol of ciphertext paired with ith symbol of key
    plaintext =''
    for (x,y) in xor_tuples_list:
        plaintext += chr(ord(x) ^ ord(y))       
    return plaintext

print(xor_decrypt(xor_encrypt(data, mykey),mykey))


