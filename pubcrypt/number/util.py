from math import floor, log2, ceil
from random import getrandbits
from math import ceil


def RBG(nBits):
    """ return a byte string of nBits"""
    return int_to_string(getrandbits(nBits), ceil(nBits/8))


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


def GCD(x,y):
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
        q <<= 2   # Equivalent to q *= 4, but using bitwise shift for better performance

    z, r = x, 0
    while q > 1:
        q >>= 2   # Equivalent to q //= 4, but using bitwise shift for better performance
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


def int_to_string(x, xLen, order="big"):
    """
    Converts a nonnegative integer to an octet string (bytes) of a specified length

    params:
        x: the integer
        xLen: len of the output
        order: big-endian (big) or little-endian (little). By default I use big-endian
    """
    result = bytearray(xLen)

    for i in range(xLen):
        byte = x & 0xff
        result[xLen-i-1] = byte
        x >>= 8

    if order == "little": 
        result = result[::-1]
    return bytes(result)


def string_to_int(x, order="big"):
    """
    Converts an octet string (bytes) to a integer

    params:
        x: the octet string
    """
    if order == "little":
        x = x[::-1]
    n = 0
    for byte in x:
        n <<= 8
        n += byte
    return n

def int_to_bin(n, iter="big"):
    result = ""
    
    while n > 0:
        bit = n & 1  # Obtient le bit le plus à droite de n
        result += str(bit)
        n = n >> 1   # Décalage de n vers la droite d'une position (équivalent à n // 2)

        bit = n & 1  # Obtient le bit le plus à droite de n
        result += str(bit)
        n = n >> 1   # Décalage de n vers la droite d'une position (équivalent à n // 2)

    if iter == "little":
        return result[::-1][::-1]
    else:
        return result[::-1]
