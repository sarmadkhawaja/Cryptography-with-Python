def transpose(message, key):
    ciphertext = ''
    for i in range(key):        
        for j in range(i, len(message), key):
            ciphertext += message[j]
    return ciphertext

print(transpose('Common sense is not so common.', 8))

