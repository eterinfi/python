from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

l = range(1, 11)
f = filter(is_prime,l)
print f
print 'Total: %d', f.__len__()