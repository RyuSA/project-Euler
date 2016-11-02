import time

start = time.time()

def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n%2 == 0:
        return False

    else:
        flag = True

        for i in xrange(3,int(n**0.5+1),2):

            if n%i == 0:
                flag = False
                break

        return flag

num = 2000000
sum = 0

for i in xrange(num):
    if is_prime(i) == True:
        sum += i

endtime = time.time() - start

print sum,endtime
