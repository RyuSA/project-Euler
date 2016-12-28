
digit = pow(10,10)
ans = 0

for n in xrange(1,1000):
    temp = pow(n,n,digit)
    ans += temp

print ans % digit
