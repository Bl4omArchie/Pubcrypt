from pubcrypt.cryptosystem.rsa import generate
import time


def get_time(n, nBits):
    result = []

    for _ in range(n):
        start_time = time.time()
        generate(nBits)
        result.append(time.time() - start_time)
    return result