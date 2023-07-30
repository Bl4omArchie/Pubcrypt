import time, random


min = pow(2, 1023)
max = pow(2, 1024)


def get_time_isqrt(n):
    result_old = []
    result_new = []

    for _ in range(n):
        start_time = time.time()
        isqrt(random.randint(min, max))
        result_old.append(time.time() - start_time)

    for _ in range(n):
        start_time = time.time()
        isqrt_binary(random.randint(min, max))
        result_new.append(time.time() - start_time)
    return result_old, result_new


def isqrt_binary(x):
    q = 1
    while q <= x: 
        q <<= 2   # Equivalent to q *= 4, but using bitwise shift for better performance

    z, r = x, 0
    while q > 1:
        q >>= 2   # Equivalent to q //= 4, but using bitwise shift for better performance
        t, r = z - r - q, r >> 1   # Equivalent to r //= 2, but using bitwise shift for better performance
        if t >= 0:
            z, r = t, r + q
    return r


def isqrt (x):
    """ Credit: https://rosettacode.org/wiki/Isqrt_(integer_square_root)_of_X#Python """
    q = 1
    while q <= x : 
        q *= 4

    z, r = x, 0
    while q > 1 :
        q //= 4
        t, r = z-r-q, r//2
        if t >= 0 :
            z, r = t, r+q
    return r 