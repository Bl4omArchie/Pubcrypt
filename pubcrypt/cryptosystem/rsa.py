from pubcrypt.number.primality import get_prime_factor
from pubcrypt.number.util import *
from random import randrange


def generate(nBits, e=65537):
    if nBits < 2048:
        raise ValueError(("Incorrect key length. nBits must be equal or greater than 2048"))
    
    elif e%2 == 0 or not 2**16 <= e <= 2**256:
        raise ValueError("Incorrect puclic exponent. e must be odd and in the range [2^16, 2^256]")
    pBits = nBits//2
    
    p, q = get_prime_factor(pBits, e) 
    d = invmod(e, lcm(p-1, q-1))
    n = p*q

    #perform a consistency test to insure the validity of the key
    m = 0x1e29b0d770e07177581a3ff4f882b1d4cbfe4fcec4f1646aec09a0fa9ba8b67fe1690c27
    if m != fast_exp_mod(m, e*d, n):
        raise ValueError("[!] Error, please retry. Consistency test failed")
    
    return n, e, d


def primitive_exp(m, exp, n):
    if 0 < m < n-1:
        return fast_exp_mod(m, exp, n)
    else:
        raise ValueError("Data representative out of range")


def crt_decrypt(ciphertext, n, e, d):
    p, q = prime_recovery(n, e, d)
    dp = d % (p - 1)
    dq = d % (q - 1)
    q_inv = invmod(q, p)
    m1 = fast_exp_mod(ciphertext, dp, p)
    m2 = fast_exp_mod(ciphertext, dq, q)

    h = (q_inv * (m1 - m2)) % p
    return m2 + h * q   #return plaintext


def prime_recovery(n, e, d):
    """ Recover the primes factor p and q that compose N """
    a = (d * e - 1) * gcd(n - 1, d * e - 1)
    m = a // n
    r = a - m * n
    b = (n - r) // (m + 1) + 1

    if b**2 <= (n << 2):
        raise ValueError("Error")

    y = isqrt(b**2 - (n << 2))
    return (b + y) >> 1, (b - y) >> 1