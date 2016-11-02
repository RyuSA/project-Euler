# coding: utf-8
def divisor_sum(num):
    div_sum = 0
    for i in xrange(1,num):
        if num % i == 0:
            div_sum += i
    return div_sum

# change a,b in this algorithm
def check_existance(number):
    a,b = number,divisor_sum(number)
    c = divisor_sum(b)
    if a == c and a != b:
        return a + b
    else :
        return False

limit = 10000
total_sum = 0

for i in xrange(1,limit):
    result = check_existance(i)
    if result:
        total_sum += result

print total_sum/2
