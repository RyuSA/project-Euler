
helper = [1,1,2,3,5,7]
flag = True
n = 6

def counter(n,t):
    # flag_counter = True
    ans = 1
    t2 = n - t
    numbers = []
    while True:
        if t2 > t:
            numbers.append(t)
            print numbers
        elif t2 == t:
            numbers.append(t)
            # numbers.append(1)
            print numbers
            return getScore(numbers)
        else:
            numbers.append(t2)
            print numbers
            return getScore(numbers)
        t2 = t2 -t


def getScore(List):
    ans = 1
    for i in List:
        ans *= helper[i]
    return ans

# while flag:
#     """
#     Example : n = 6
#     count is 1 (6 = 6 (+0))
#     """
#     count = 1
#     for k in reversed(xrange(n)):
#         temp = n - k
#         if n < temp:
#             sum_flag = True
#             summation = [temp]
#             a = 1
#             while sum_flag:
#                 summation[0] -= 1
#                 summation.append()
#         elif n == temp:
#
#         else:
#             count += helper[temp]
#
print counter(16,4)
