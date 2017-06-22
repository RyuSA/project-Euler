from fractions import Fraction
from itertools import product

ans = []
for x,y in product(range(10,100),range(10,100)):

    if x >= y:
        continue

    frac = Fraction(x,y)

    temp_x = [int(m) for m in list(str(x))]
    temp_y = [int(m) for m in list(str(y))]

    if temp_y[1] == 0:
        continue

    if temp_x[0] == temp_y[0]:
        if frac == Fraction(temp_x[1],temp_y[1]):
            ans.append([x,y])
            continue
    if temp_x[1] == temp_y[0]:
        if frac == Fraction(temp_x[0],temp_y[1]):
            ans.append([x,y])
            continue
    if temp_x[0] == temp_y[1]:
        if frac == Fraction(temp_x[1],temp_y[0]):
            ans.append([x,y])
            continue
    if temp_x[1] == temp_y[1]:
        if frac == Fraction(temp_x[0],temp_y[0]):
            ans.append([x,y])
            continue

ans_a, ans_b = 1,1
for a,b in ans:
    ans_a *= a
    ans_b *= b

print ans_b/ans_a
