
# An = [2]
# Bn = [2*(x-1) if x%3 == 2 else 1 for x in xrange(200)]
# An = An + Bn
An = [2]
Pn = [2,3]
counter = 1
for x in xrange(1,200):
    if x%3 == 2:
        An.append(2*counter)
        counter += 1
    else :
        An.append(1)
    if x != 1:
        Pn.append(An[x]*Pn[x-1]+Pn[x-2])

N = Pn[100-1]
print sum(map(lambda x : int(x) , list(str(N))))
