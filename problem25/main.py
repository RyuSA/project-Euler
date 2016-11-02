import math
f1 = 1
f2 = 1
count = 2
while True:
    count += 1
    temp = f1 + f2
    if math.log(temp,10) >= 999:
        break
    f1,f2 = f2,temp
print count
