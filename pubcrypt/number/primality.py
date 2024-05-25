from random import randrange, getrandbits
from pubcrypt.number.lib import PAL, GMP


round = 5

def get_prime_factors(pBits, e, library=PAL()):
    """ Generate a prime factor """ 
    i = 0
    candidate = library.integer()

    while candidate == 0:
        while i < (5 * pBits):
            p = library.random_number(pBits)
            if p & 1 == 0:  #if the number is odd, add one
                p |= 1 

            if p >= (library.isqrt(2) << (pBits - 1)):
                if library.gcd(p-1, e) == 1:
                    candidate = miller_rabin(p, round)
                    break
            i += 1

    i = 0
    candidate = 0
    while candidate == 0:
        while i<5*pBits:
            q = library.random_number(pBits)
            if q & 1 == 0:
                q |= 1

            if (abs(p-q) > pow(2, (pBits//2)-100)) or (q >= (library.isqrt(2) << (pBits - 1))):
                if library.gcd(q-1, e) == 1:
                    candidate = miller_rabin(q, round)
                    break
            i += 1
    return p, q


def miller_rabin(p, r):
    s, d = 0, p - 1
    while d & 1 == 0:
        d >>= 1
        s += 1

    for _ in range(r):
        a = randrange(2, p - 2)
        x = library.powmod(a, d, p)
        if x == 1 or x == p - 1:
            continue
        for _ in range(s - 1):
            x = library.powmod(x, 2, p)
            if x == p - 1:
                break
        else:
            return 0

    return 1