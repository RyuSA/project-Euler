latter = [1]
former = []
value = 1000000
count = 0

def nCr(n,r):
    if r == 0 or r == n:
        return 1
    else:
        return latter[r-1] + latter[r]

def countIF(List):
    return len([x for x in List if x >= value])

for n in xrange(100+1):
    for r in xrange(n+1):
        temp = nCr(n,r)
        former.append(temp)
    latter = former[:]
    print latter
    count += countIF(latter)
    former = []

print count
