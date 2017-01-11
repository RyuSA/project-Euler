import integer

primes = [n for n in xrange(1,10000,2) if integer.isPrime(n)]
primes.append(2)
primes.sort()
ans = 1
target = 1000000
temp = []
for prime in primes:

    ans = integer.mult(temp)
    if ans*prime < target:
        temp.append(prime)
    else :
        break

print temp, integer.mult(temp)
