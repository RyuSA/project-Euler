# coding: utf-8
import math

def Primes(n):
    if n == 1:
        return False
    else:
        flag = True
        for i in range(2,n):
            if n%i == 0:
                flag = False
                break
        return flag

num = 600851475143
Max = int(math.sqrt(num))
prime = 1

for i in range(1,Max):
    if num % i ==0 and Primes(i) == True:
        print i
        prime = i

print prime, prime*(num/prime), Primes(prime)
