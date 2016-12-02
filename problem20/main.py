target = 1
for i in xrange(2,100):
    if i % 10 == 0:
        target *= (i/10)
    else :
        target *= i
digits = [int(x) for x in str(target)]
print sum(digits)
