#Find greatest common divisor of 2 integers a and b
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#Use Euclid's Extended Euclid Algorithm to find modular inverse of a number 'a'
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None  # No mod inverse if a & m aren't relatively prime.
    x, y, z = 1, 0, a
    i, j, k = 0, 1, m
    while k != 0:
        q = z // k  # Note that // is the integer division operator.
        i, j, k, x, y, z = (x - q * i), (y - q * j), (z - q * k), i, j, k
    return x % m
