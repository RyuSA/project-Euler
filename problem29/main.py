#coding : utf-8;

squeres = []
maximum = 100

for a in xrange(2,maximum+1):
    for b in xrange(2,maximum+1):
        temp = pow(a,b)
        if temp in squeres:
            continue
        else :
            squeres.append(temp)

squeres.sort()

print len(squeres)
# print squeres
