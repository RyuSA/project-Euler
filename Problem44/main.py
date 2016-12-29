pentagon = [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]
flag = True
count = 0
def addNewPenta(lista):
    lista.append(lista[-1]+3*len(lista)+1)


while flag:
    addNewPenta(pentagon)
    # print pentagon
    for i in xrange(len(pentagon)-2):
        for j in xrange(i,len(pentagon)-1):
            if pentagon[i] + pentagon[j] == pentagon[-1]:
                # print pentagon
                if abs(pentagon[j] - pentagon[i]) in pentagon:
                    print pentagon[i], pentagon[j]
                    print abs(pentagon[j]-pentagon[i])
                    count +=1
    if count > 50:
        flag = False
