from pubcrypt.number.primality import get_prime_factor
from pubcrypt.number.util import *
from random import randrange


def generate(nBits, e=65537):
    if nBits < 2048:
        raise ValueError(("Incorrect key length. nBits must be equal or greater than 2048"))
    
    elif e%2 == 0 or not pow(2, 16) <= e <= pow(2, 256):
        raise ValueError("Incorrect puclic exponent. e must be odd and in the range [2^16, 2^256]")

    pBits = nBits//2
    
    p = get_prime_factor(pBits, e) 
    q = get_prime_factor(pBits, e)
    d = invmod(e, lcm(p-1, q-1))
    n = p*q

    if pair_wise_consistency_test(n, e, d) == 0:
        raise ValueError("Error, please retry. Consistency test failed")

    return n, e, d


def primitive_exp(m, exp, n):
    """ This function represent the encryption/decryption/signature operation """
    if 0 < m < n-1:
        return pow_mod(m, exp, n)

    else:
        raise ValueError("Data representative out of range")


def prime_recovery(n, e, d):
    """ Recover the primes factor p and q that compose N """
    a = (d*e-1) * gcd(n-1, d*e-1)
    m = a//n
    r = a - m*n
    b = (n-r) // (m+1) +1

    if pow_mod(b, 2) <= 4*n:
        raise ValueError("Error")

    y = isqrt(pow_mod(b, 2)-4*n)
    return (b+y) // 2, (b-y) // 2


def pair_wise_consistency_test(n, e, d):
    """ Check if the generated keypair can encrypt and decrypt correctly a plaintext m """
    m = randrange(1, n//2)
    return m == primitive_exp(m, e*d, n)