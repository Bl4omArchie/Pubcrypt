from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.util import *
from pubcrypt.number.primality import *
import concurrent.futures


def generate_multi_keypair(num_keys, num_proc, nBits, e=65537):
    Queue = []
    key_pairs = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while len(key_pairs) < num_keys:
            for _ in range(num_proc):
                Queue.append(executor.submit(generate, nBits, e))

            for proc in Queue:
                key_pairs.append(proc.result())
                Queue.remove(proc)

    return key_pairs