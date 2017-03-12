
def find_it_and_get_insert(List, target):
    # the list is ordered
    low = 0
    high = len(List)
    t = (low + high) // 2

    while True:
        if (target==List[t]):
            return False
        elif (target > List[t]):
            low = t + 1
        elif (target < List[t]):
            high = t - 1
        if (high - low == 1):
            return [low-1,high-1]
        t = (low + high) // 2

# maximum = 10000000
maximum = 100
for i in range(maximum):
    target = list(map(lambda x: pow(int(x),2), list(str(i))))
    target = sum(temp)
    while find_it_and_insert(temp,)

test = [1,2,3,4,5,6,8]
print(find_it_and_insert(test,7))
