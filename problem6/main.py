def sqrsum(n):
    return n*(n+1)*(2*n+1)/6

def sumsqr(n):
    return (n*(n+1)/2)**2

N = 100

print sumsqr(N)-sqrsum(N)
