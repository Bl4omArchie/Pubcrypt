from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.util import *
from pubcrypt.number.primality import *
import concurrent.futures


def generate_key_pairs(nBits, e=65537):
    if nBits < 2048:
        raise ValueError("Incorrect key length. nBits must be equal or greater than 2048")
    
    elif e % 2 == 0 or not pow_fast(2, 16) <= e <= pow_fast(2, 256):
        raise ValueError("Incorrect public exponent. e must be odd and in the range [2^16, 2^256]")
    
    pBits = nBits // 2
    p, q = get_prime_factors(pBits, e) 
    d = invmod(e, lcm(p-1, q-1))
    n = p * q

    if pair_wise_consistency_test(n, e, d) == 0:
        raise ValueError("Error, please retry. Consistency test failed")
    
    return n, e, d

def generate_multi_keypair(num_keys, num_proc, nBits, e=65537):
    Queue = []
    key_pairs = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while len(key_pairs) < num_keys:
            for _ in range(num_proc):
                Queue.append(executor.submit(generate_key_pairs, nBits, e))

            for proc in Queue:
                key_pairs.append(proc.result())
                Queue.remove(proc)

    return key_pairs