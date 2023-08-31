import gmpy2, os
from gmpy2 import mpz, isqrt, gcd, powmod


r = 5

def get_prime_factor(pBits, e, state):
    """ Generate a prime factor """
    i = 0
    candidate = mpz(0)

    while candidate == 0:
        while i < (5 * pBits):
            p = gmpy2.mpz_random(state, 2 ** pBits)
            if p & 1 == 0:  # if the number is odd, add one
                p |= 1

            if p >= (isqrt(2) << (pBits - 1)):
                if gcd(p - 1, e) == 1:
                    candidate = miller_rabin(p, r, state)
                    break
            i += 1

    i = 0
    candidate = mpz(0)
    while candidate == 0:
        while i < 5 * pBits:
            q = gmpy2.mpz_random(state, 2 ** pBits)
            if q & 1 == 0:
                q |= 1

            if (abs(p - q) > pow(2, (pBits // 2) - 100)) or (q >= (isqrt(2) << (pBits - 1))):
                if gcd(q - 1, e) == 1:
                    candidate = miller_rabin(q, r, state)
                    break
            i += 1
    return p, q

def miller_rabin(p, r, state):
    s, d = 0, p - 1
    while d & 1 == 0:
        d >>= 1
        s += 1

    for _ in range(r):
        a = gmpy2.mpz_random(state, p - 3) + 2
        x = powmod(a, d, p)
        if x == 1 or x == p - 1:
            continue
        for _ in range(s - 1):
            x = powmod(x, 2, p)
            if x == p - 1:
                break
        else:
            return 0

    return 1