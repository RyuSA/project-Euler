import time

def poly(n):
    return 16*n*n + 4*n + 4

def S(n):
    if n == 2:
        return 25
    return S(n-1) + poly(n-1)

start = time.time()
print S(501),time.time()-start
