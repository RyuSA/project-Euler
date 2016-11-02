import time

start = time.time()

Fib = [1,2]
deadline = 4000000
sum = 2

while True:

    newFib = Fib[0]+Fib[1]
    Fib[0] = Fib[1]
    Fib[1] = newFib

    if Fib[1] > deadline :
        break

    print Fib[0],Fib[1]

    if newFib % 2 == 0:
        sum += newFib

print sum, time.time()-start
