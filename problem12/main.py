import time
import numpy as np

start = time.time()

num = 100
i = 1

while True:
    
    divisor = np.array([])
    triangle_number = i*(i+1)/2
    # print "triangle_number is",triangle_number

    for j in xrange(1,triangle_number+1):

        if triangle_number%j == 0:

            divisor = np.append(divisor,[j])
            # print divisor, len(divisor)

    if divisor.size >= num:
                break
    i += 1

print triangle_number, time.time()-start
