
def isPythagorean(a,b,c):
    if a < b < c:
        return pow(a,2) + pow(b,2) == pow(c,2)
    else :
        return False

for i in xrange(1,998):
    for j in xrange(1,998-i):
        k = 1000 - i - j
        if isPythagorean(i,j,k):
            print i*j*k
print 'done'
