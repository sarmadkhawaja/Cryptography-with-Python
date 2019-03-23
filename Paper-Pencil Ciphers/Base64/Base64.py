import base64
mystring = 'Hello'
mystring_in_binary = mystring.encode('utf-8')
mystring_in_base64 = base64.b64encode(mystring_in_binary)
print("Encoded text with base 64 is")
print(mystring_in_base64)

mystring_in_ascii = base64.b64decode(mystring_in_base64)
print(mystring_in_ascii)



