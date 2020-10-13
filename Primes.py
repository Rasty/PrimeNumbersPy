## Python Prime Number Generator ##

import math

primes = []

def isPrime(PrimesNumber):
       if PrimesNumber<=1:
           return False
       if PrimesNumber==2:
           return True
       if PrimesNumber%2==0:
           return False
       for ind in range(3,int(math.sqrt(PrimesNumber))+1):
           if PrimesNumber%ind==0:
               return False
       return True

for i in range (1, 1000):
       if isPrime(i) == True:
           primes.append(i)
       else:
           continue

print(primes)

