# coding : UTF-8;
import integer
import numpy as np

primes = []
squares = [1]

count = 1
flag = True

while flag:
    count += 1
    # print primes, squares
    squares.append(count*count)
    if integer.isPrime(count):
        primes.append(count)
    elif count & 1 :
        for prime in primes:
            for square in squares:
                temp = prime + 2*square
                if temp > count:
                    break
                if count == temp:
                    flag = False
                    print count, prime, 2*square
                    continue
            if not flag:
                break
        if flag:
            print "found it!!"
            print count
            break
        else :
            flag = True
