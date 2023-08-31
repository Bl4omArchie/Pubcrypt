import gmpy2, os, random
from gmpy2 import mpz, isqrt, gcd, powmod, random_state, lcm
from pubcrypt.number.primality_GMP import get_prime_factor


def generate_gmp(nBits, e=65537):
    if nBits < 2048:
        raise ValueError("Incorrect key length. nBits must be equal or greater than 2048")
    
    elif e % 2 == 0 or not pow(2, 16) <= e <= pow(2, 256):
        raise ValueError("Incorrect public exponent. e must be odd and in the range [2^16, 2^256]")
    
    pBits = nBits // 2
    random.seed(int.from_bytes(os.urandom(32), byteorder='big'))
    state = random_state()
    
    p, q = get_prime_factor(pBits, e, state)
    d = powmod(e, -1, lcm(p - 1, q - 1))
    n = p * q

    if pair_wise_consistency_test(n, e, d, state) == 0:
        raise ValueError("Error, please retry. Consistency test failed")
    return n, e, d


def primitive_exp(m, exp, n):
    """ This function represents the encryption/decryption/signature operation """
    if 0 < m < n - 1:
        return powmod(m, exp, n)
    else:
        raise ValueError("Data representative out of range")


def prime_recovery(n, e, d):
    """ Recover the prime factors p and q that compose N """
    a = (d * e - 1) * gcd(n - 1, d * e - 1)
    m = a // n
    r = a - m * n
    b = (n - r) // (m + 1) + 1

    if pow(b, 2) <= (n << 2):
        raise ValueError("Error")

    y = isqrt(pow(b, 2) - (n << 2))
    return (b + y) >> 1, (b - y) >> 1


def pair_wise_consistency_test(n, e, d, state):
    """ Check if the generated keypair can encrypt and decrypt correctly a plaintext m """
    m = gmpy2.mpz_random(state, n // 2) + 1
    return m == primitive_exp(m, e * d, n)
