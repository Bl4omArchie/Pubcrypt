from pubcrypt.number.util import gcd, isqrt, pow_fast
from pubcrypt.number.util import RNG
from random import randint


def get_prime_factor(pBits, e):
    """ Generate a prime factor """ 
    i = 0
    candidate = 0

    while candidate == 0:
        while i < (5 * pBits):
            p = RNG(pBits)
            if p & 1 == 0:
                p |= 1   # Ensure p is odd (set the least significant bit to 1)

            if p >= (isqrt(2) << (pBits - 1)):
                if gcd(p - 1, e) == 1:
                    candidate = miller_rabin(p, 5)
                    break
            i += 1
    return p


def miller_rabin(p, r):
    s, d = 0, p - 1
    while d & 1 == 0:
        d >>= 1
        s += 1

    for _ in range(r):
        a = randint(2, p - 2)
        x = pow_fast(a, d, p)
        if x == 1 or x == p - 1:
            continue
        for _ in range(s - 1):
            x = pow_fast(x, 2, p)
            if x == p - 1:
                break
        else:
            return 0

    return 1