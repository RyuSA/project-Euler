# coding : utf-8;
import integer

def getQuadSeq(a,b):
    if integer.isPrime(b):
        n = 1
        temp = a+b+1
        count = 1
        if integer.isPrime(temp):
            count += 1
            while True:
                n += 1
                temp += 2*n+a-1
                if integer.isPrime(temp):
                    count += 1
                else :
                    return count

        else :
            return count
    else :
        return 0

maximum = 1
for i in xrange(-1000,1000):
    for j in xrange(-1000,1001):
        temp = max(maximum,getQuadSeq(i,j))
        if temp > maximum:
            maximum = temp
            target = i*j

print target
