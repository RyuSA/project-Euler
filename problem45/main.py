import math

def mPn(n):
    return n*(3*n-1)

def mTn(n):
    return n*(n+1)

def mHn(n):
    return 4*n*n-2*n

def isTn(a):
    deadline = int(math.floor(math.sqrt(0.25+a)))
    for i in xrange(deadline-1,deadline+2):
        if mTn(i) == a:
            return i
    return False

def isHn(a):
    deadline = int(math.floor(0.5*math.sqrt(a)))
    for i in xrange(deadline-1,deadline+2):
        if mHn(i) == a:
            return i
    return False

init = 150
temp = mTn(init)
M = 100000

for k in xrange(init,M):
    temp = mPn(k)
    if isTn(temp) and isHn(temp):
        print temp/2
print "done"
