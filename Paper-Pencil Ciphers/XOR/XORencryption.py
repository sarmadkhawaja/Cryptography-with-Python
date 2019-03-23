from itertools import cycle
import base64

def xor_encrypt(message, key):
    xor_tuples_list = list(zip(message,cycle(key))) #each tuple in the list contains ith symbol of message paired with ith symbol of key
    ciphertext =''
    for (x,y) in xor_tuples_list:
        ciphertext += (chr(ord(x) ^ ord(y)))
        ciphertext_in_bytes = ciphertext.encode('utf-8')
        ciphertext_in_base64 = base64.b64encode(ciphertext_in_bytes)
    return ciphertext_in_base64





data = "XOR procedure"
mykey = 'awesomepassword'

print(xor_encrypt(data,mykey))







