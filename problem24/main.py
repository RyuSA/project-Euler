from math import factorial

factors = [factorial(x) for x in range(1,10)]
factors.reverse()
temp = []
maximun = 1000000

# 階乗で1000000を削っていく
# n進数を求めるような作業
for factor in factors:
    index = 0
    while maximun > 0:
        maximun = maximun - factor
        index = index + 1
    temp.append(index-1)
    maximun = maximun + factor


# 0～9までを割り当てる
R = list(range(10))
ans = []

for i in temp:
    ans.append(R.pop(i))
ans.append(R.pop(0))
ans.reverse()

# 解答出力用
answer = 0
power = 0
for i in ans:
    answer = answer + i*pow(10,power)
    power = power + 1
print(answer)
