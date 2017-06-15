
ans = 0
ans_d = 0

maximum = 1000

def getIndex(List,target):
    List.append(target)
    i = 0
    while List[i] != target:
        i = i+1
    if i == len(List)-1:
        return -1
    else :
        return i

for b in range(1,maximum+1):
    a = 10
    temp = []
    r = 0
    q = 1
    while True:
        q = a // b
        if q == 0:
            temp.append(0)
            a = a*10
            continue
        r = a - b*q
        if r == 0 :
            break
        if a in temp :
            length = len(temp) - getIndex(temp,a)
            if ans < length:
                ans = length
                ans_d = b
            break
        temp.append(a)
        a = r*10

print(ans)
print(ans_d)
