from pubcrypt.cryptosystem.rsa import generate



def bench_generate(n, nBits, e=65537):
    """ generate n times a nBits bit size key """
    for _ in range(n):
        generate(nBits)


def bench_is_prime(n, pBits):
    pass


def bench_gcd(n):
    pass