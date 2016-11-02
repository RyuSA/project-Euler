# coding: utf-8

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

for i in xrange(900,999):
    for j in xrange(900,999):
        temp = i*j
        if is_palindrome(temp):
            print temp
