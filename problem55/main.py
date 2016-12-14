
total = 10000
maximum = 50


def reverse_number(integer):
    return int(str(integer)[::-1])

def isPalindrome(integer):
    if integer == reverse_number(integer):
        return True
    else :
        return False

def isLycherel(integer):
    for counter in xrange(maximum):
        temp = integer+reverse_number(integer)
        # print temp
        if isPalindrome(temp):
            return False
        else:
            integer = temp
    return True

count = 0
for i in xrange(total):
    if isLycherel(i):
        count += 1

print count
