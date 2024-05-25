from math import floor, log2, ceil
from pubcrypt.number.util import get_length

def invmod  (u, v):
    if not u < v:
        u, v = v, u

    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        q = u3 // v3
        u1, v1 = v1, u1 - v1*q
        u3, v3 = v3, u3 - v3*q
    if u3 != 1:
        raise ValueError("No inverse value can be computed")
    while u1<0:
        u1 = u1 + v
    return u1


def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    x_z = (x & -x).bit_length()-1
    y_z = (y & -y).bit_length()-1
    shift = min(x_z, y_z)
    y_z >>= y_z

    while x != 0:
        x >>= x_z
        diff = y-x
        x_z = (diff & -diff).bit_length()-1
        y = min(x, y)
        x = abs(diff)

    return y << shift


def gcd_basic(x,y):
    """Greatest Common Denominator of :data:`x` and :data:`y`."""
    x = abs(x) ; y = abs(y)
    while x > 0:
        x, y = y % x, x
    return y


def lcm(x, y):
    return (x*y) // gcd(x, y)


def fast_exp_mod(b, e, m):
    result = 1
    b %= m  
    while e > 0:
        if e & 1:
            result = (result * b) % m
        b = (b * b) % m
        e >>= 1
    return result % m


def isqrt (x):
    q = 1
    while q <= x: 
        q <<= 2                    # Equivalent to q *= 4, but using bitwise shift for better performance

    z, r = x, 0
    while q > 1:
        q >>= 2                    # Equivalent to q //= 4, but using bitwise shift for better performance
        t, r = z - r - q, r >> 1   # Equivalent to r //= 2, but using bitwise shift for better performance
        if t >= 0:
            z, r = t, r + q
    return r


def perfect_square(c):
    n = floor(log2(abs(c))) + 1
    m = ceil(n/2)
    x = pow(2, m) - pow(2, m-1)

    while True:
        x = (pow(x, 2)+c)/(2*x)
        if pow(x, 2) < pow(2, m)+c:
            break

    return c == pow(floor(x), 2)

# Using bit wise operators clearly improve performance. See graph in benchmark/graph/
def karatsuba(x,y):
    if x < 10 and y < 10:
        return x*y

    n = max(get_length(x), get_length(y))
    m = (n + 1) >> 1

    x_H = x >> m
    x_L = x & ((1 << m)-1)

    y_H = y >> m
    y_L = y & ((1 << m)-1)

    a = karatsuba(x_H, y_H)
    d = karatsuba(x_L, y_L)
    e = karatsuba((x_H + x_L), (y_H + y_L)) - a - d

    return (a << (m << 1)) + ((e << m) + d)

def karatsuba2(x,y):
    if x < 10 and y < 10:
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)   #Cast n into a float because n might lie outside the representable range of integers.

    x_H  = floor(x / pow(10, m))
    x_L = x % pow(10, m)

    y_H = floor(y / pow(10, m))
    y_L = y % pow(10, m)

    a = karatsuba2(x_H,y_H)
    d = karatsuba2(x_L,y_L)
    e = karatsuba2(x_H + x_L, y_H + y_L) - a - d

    return int(a*pow(10, m*2) + e*pow(10, m) + d)