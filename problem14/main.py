#
def collatz(n):
    if n == 1:
        return -1
    if n&1:
        return 3*n+1
    else :
        return n >> 1

mil = 1000000
# vector[k+1] has the number of k-th chain
vector = [1]*mil
# Example
vector[0] = 1
# 2 > 1
vector[1] = 2
# 3 > 10 > 5 > 16 > 8 > 4 > 2 > 1
vector[2] = 8
for index in xrange(3,mil):
    count = 1
    n = index + 1
    while True:
        temp = collatz(n)
        if temp == 1:
            vector[index] = count
            break
        # if i is odd, temp must be greater than i
        if n&1:
            count += 1
        # if i is even, temp must be less than i
        else :
            if temp < index:
                count += vector[temp-1]
                vector[index] = count
                break
            else:
                count += 1
        n = temp
print vector.index(max(vector))+1
