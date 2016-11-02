# coding: utf-8

def gcd(a,b):
    while b:
        a , b = b , a%b
    return a

def lcm(a,b):
    return a*b/gcd(a,b)


max = 20
vector = range(2,max+1)

ini = 1
for i in vector:
    ini = lcm(ini,i)
print ini
