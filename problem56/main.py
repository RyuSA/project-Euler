
maximum = 0

for a in xrange(1,100):
    for b in xrange(1,100):
        temp = pow(a,b)
        temp_list = [int(n) for n in list(str(temp))]
        temp_sum = sum(temp_list)
        maximum = max(maximum,temp_sum)

print maximum
