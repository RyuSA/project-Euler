#coding:utf-8
import random

def MillerRabin(n):
    # Miller–Rabin primality test
    # if p is even or minus, return False
    # ignore 2
    if (not n&1) or (n < 0) or n == 1 :
        return False

    # n = 2^s * d + 1
    s = 1
    d = (n-1) >> 1
    while not d&1:
        # d is divided by 2
        d = d >> 1
        # upgrade s
        s += 1

    # this number is related to sucsess probability
    # probability ~ (25%)^times
    times = 10

    for i in xrange(times):
        # flag will be used for line 43
        flag = True
        # b is a base
        b = random.randint(2,n-1)
        # X = b^d mod n
        X = pow(b,d,n)

        # if X is 1 or -1, then this 'b' pass the test. go next b
        if X == 1 or X == n-1:
            continue

        for j in xrange(s):
            X = pow(X,2,n)
            # X = b^(2r)d mod n
            if X == n-1:
                # pass the test, go next b
                flag = False
                break
        if flag:
            # flag has not been modifyied, which mean we never obtain -1
            return False

    # pass times times text, this n may be prime number
    return True

def isPrime(n):
    """Miller Rabin Test -> trial division"""
    # if n is 2 or 3, return True
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if MillerRabin(n):
        # n is MAYBE prime number
        Upper = int(pow(n,0.5))
        for i in xrange(5,Upper,6):
            if n%i == 0 or n%(i+2) == 0:
                return False
        del Upper
        return True
    return False

def gcd(a,b):
    while b :
        a , b = b , a%b
    return a

def lcm(a,b):
    return a*b / gcd(a,b)

def extendEuclid(a,b):
    """find the integers x,y such that xa + yb = 1"""
    flag = False
    if a < b:
        a ,b = b, a
        flag = True
    if b == 0:
        x = 1
        y = 0
    else :
        # e = 1 << 16 +1
        q = a/b
        r = a%b
        (u,v) = extendEuclid(b,r)
        x = v
        y = u - q*v
    if flag:
        return (y,x)
    return (x,y)
