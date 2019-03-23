import math, random

##################################################################################
#check if a number is prime using trial division on numbers upto square root of that number
def isPrimeTrialDiv(num):

#uses trial division to determine if a number is prime

    if num < 2:
        return False

#check if number is divisible by any other number upto sqrt of the number

    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True
##################################################################################
#generate a list of prime numbers upto sievesize 
def primeSieve(sievesize):

    #initialize list of Boolean values indicating which numbers in the range 1-sievesize are prime
    sieve = [True]*sievesize
    sieve[0] = False
    #change value to False for those indices of sieve that are multiples of integers in the range 2-sqrt(num)
    for i in range(2,int(math.sqrt(sievesize)+1)):
        j = 2
        while (i*j) <= sievesize:
            sieve[i*j - 1] = False
            j+=1
    #compile the list of primes
    primes = []
    for k in range(sievesize):
        if sieve[k] == True:
            primes.append(k+1)
    return primes
##################################################################################  
def rabinmiller(num):
    # returns true if num is a prime number.
    if num % 2 == 0 or num < 2:
        return false # rabin-miller doesn't work on even integers.
    if num == 3:
        return true
    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s until it is odd (and use t
        # to count how many times we halve s):
        s = s // 2
        t += 1
    for trials in range(5): # try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True
##################################################################################
# Most of the time we can quickly determine if num is not prime
# by dividing by the first few dozen prime numbers. This is quicker
# than rabinMiller() but does not detect all composites.
LowPrimes = primeSieve(100)

def isPrime(num):
# Return True if num is a prime number. This function does a quicker
# prime number check before calling rabinMiller().
    if (num < 2):
        return False # 0, 1, and negative numbers are not prime.
# See if any of the low prime numbers can divide num:     
    for prime in LowPrimes:
        if num == prime:
            return True
        elif num % prime == 0:
            return False
# If all else fails, call rabinMiller() to determine if num is prime:
    return rabinmiller(num)
##################################################################################
def generateLargePrime(keysize=1024):
    # Return a random prime number that is keysize bits in size:
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num
##################################################################################

   









            






