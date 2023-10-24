from pubcrypt.number.primality import get_prime_factors
from pubcrypt.parallel.clock import Clock

from pubcrypt.number.util import *
from multiprocessing import Process


"""
The keypairs_engine is a program that generate key pairs during a certains amount of times. 
The prime factors are constantly generated with parallelism so it can produce the most keys as possible.

1- clock
Check the time and stop the whole program when the time limit has been reached

2- generate prime factors (parallel)
Every other processus are dedicated to the prime factors generation

3- construct key-pair
Wrap the returned prime factors, generate N, phi(N), d and the CRT exponents

4- store the key
Store every data in a PEM file and store the file into a folder

"""

end_program = False
NUM_PROC = 10

def construct_key_pairs():
    while end_program == False:
        pass

def store_key():
    while end_program == False:
        pass


def keypairs_engine(time: tuple, pub_exp: int, nBits: int):
    if nBits < 2048:
        raise ValueError(("Incorrect key length. nBits must be equal or greater than 2048"))
    
    elif pub_exp%2 == 0 or not pow_fast(2, 16) <= pub_exp <= pow_fast(2, 256):
        raise ValueError("Incorrect puclic exponent. e must be odd and in the range [2^16, 2^256]")
    pBits = nBits//2

    #start clock
    clock = Clock(time)
    clock.start()

    #start generating prime factors
    processus = []
    for _ in range(NUM_PROC):
        processus.append(Process(target=get_prime_factors, args=(pBits, pub_exp)))

    #start construct key pairs
    construct_key_pairs()

    # start wrapping keys
    store_key()