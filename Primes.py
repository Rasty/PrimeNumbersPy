########################################################
#
#
#
#######################################################

import math

primes = []

def isPrime(number):
       if number<=1:
           return False
       if number==2:
           return True
       if number%2==0:
           return False
       for ind in range(3,int(math.sqrt(number))+1):
           if number%ind==0:
               return False
       return True

for i in range (1, 1000):
       if isPrime(i) == True:
           primes.append(i)
       else:
           continue

print(primes)

