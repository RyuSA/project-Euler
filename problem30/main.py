import numpy as np

List = np.array([pow(x,5) for x in xrange(10)])

def isOK(n):
    if n == sum(map(lambda x: List[int(x)], list(str(n)))):
        return True
    else:
        return False

Max = 10000000
ans = []
for x in xrange(1000,Max):
    if isOK(x):
        print x
        ans.append(x)
print sum(ans)
