# 1 < m < 250
# 1 < n < 500
# m > n

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b > 0:
        a,b = b, a%b
    return a

def returnPitago(m,n):
    # m>n
    if m <= n:
        return False
    return [m**2 - n**2, 2*m*n , m**2+n**2]

def isCorrect(List):
    a,b,c = List
    if sum(List) > maximum:
        return False
    x = gcd(a,b)
    if x != 1:
        return False
    if gcd(x,c) != 1:
        return False
    return True

maximum = 1000
ans = [0]*maximum
debug = []

for m in xrange(1,251):
    for n in xrange(1,501):
        a = returnPitago(m,n)
        if a:
            if isCorrect(a):
                debug.append(a)
                temp = sum(a)
                while temp < maximum:
                    ans[temp] += 1
                    temp += sum(a)

max_ans = 0
answer = 0
for index,value in enumerate(ans):
    if value > max_ans:
        answer = index
        max_ans = value
print answer
print ans[answer]
