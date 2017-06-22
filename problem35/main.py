from time import clock

def isCircular(prime):
    prime = [int(x) for x in str(prime)]
    temp = [int("".join(map(str,prime)))]
    for count in xrange(len(prime)-1):
        p = prime.pop(0)
        prime.append(p)
        temp.append(int("".join(map(str,prime))))

    for x in temp:
        if not table[x]:
            return False
    return True

start = clock()
maximum = 1000000

table = [1 if x & 1 else 0 for x in xrange(maximum)]
table[1] = 0
table[2] = 1
primes = [2]

for i in xrange(3,maximum,2):
    if table[i]:
        primes.append(i)
        temp = i*3
        while temp < maximum:
            table[temp] = 0
            temp += i<<1

ans = []
for prime in primes:
    if isCircular(prime):
        ans.append(prime)

print ans
print len(ans)
print str(clock()-start)
