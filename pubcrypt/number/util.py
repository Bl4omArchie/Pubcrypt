from math import floor, log2, ceil
from random import getrandbits
from math import ceil


def RBG(nBits):
    """ return a byte string of nBits"""
    return int_to_string(getrandbits(nBits), ceil(nBits/8))

def RNG(nBits):
    """ return an integer of nBits"""
    return getrandbits(nBits)


def invmod(z, a):
    if not z < a:
        z, a = a, z

    i, j = a, z
    y1, y2 = 1, 0

    while j > 0:
        q = i // j
        r = i - (j * q)
        y = y2 - (y1 * q)
        i, j = j, r
        y2, y1 = y1, y

    return y2 % a


def gcd(x, y):
    r = [x, y]
    i = 1
    while r[i] >= 0:
        i += 1
        r.append(r[i-2] % r[i-1])

        if r[i] == 0:
            return r[i-1]


def lcm(x, y):
    return (x*y) // gcd(x, y)


def pow_fast(x, e, m=None):
    result = 1
    while e > 0:
        if e & 1:
            result *= x
            if m:
                result %= m
        x *= x
        if m:
            x %= m
        e >>= 1

    if m:
        result %= m
    return result

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

    if iter == "little":
        return result[::-1]
    else:
        return result[::-1]