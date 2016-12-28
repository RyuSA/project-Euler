
# init
A = 3
B = 2
count = 0

for n in xrange(1,1000):
    A, B = A+2*B, A+B
    if len(str(A)) > len(str(B)):
        # print A,B
        count += 1

print "done"
print count
