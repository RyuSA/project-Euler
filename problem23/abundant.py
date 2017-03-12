from math import ceil
import sys

abundant = []
maximun = 28123
ans = 0

# abundantか否かを返す
def isAbundant(n):
    ans = getDivisors(n)
    return sum(ans) > n

# nの約数の集合をリストにして返す
def getDivisors(n):
    ans = [1]
    for i in range(2,ceil(pow(n,0.5)+1)):
        if n % i == 0:
            ans.append(i)
            ans.append(int(n/i))
    ans = list(set(ans))
    return ans

# abundantにabundant数を追加する
def listAbundant():
    global abundant
    for i in range(11,maximun):
        if isAbundant(i):
            abundant.append(i)

# abundantの二分探索
def search(n):
    if n < 12:
        return -1
    low = 0
    high = len(abundant)
    t = (low + high) // 2
    while (low<=high):
        if (n==abundant[t]):
            return t
        elif (n > abundant[t]):
            low = t + 1
        elif (n < abundant[t]):
            high = t - 1
        t = (low + high) // 2
    return -1

# nが二つのAbundantの和になっていればTrue : Otherwise False
def isSumOfAbundants(n):
    for i in abundant:
        if n-i< 0:
            break
        if(search(n-i) > -1):
            return True
    return False
