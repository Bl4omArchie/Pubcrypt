from pubcrypt.number.primality import get_prime_factors
from pubcrypt.number.util import *
from multiprocessing import Process
import time

NUM_PROC = 10


"""
The keypairs_engine is a program that generate key pairs during a certains amount of times. 
The prime factors are constantly generated with parallelism so it can produce the most keys as possible.

1 proc: clock
Check the time and stop the whole program when the time limit has been reached

2 proc: construct key-pair
Wrap the returned prime factors, generate N, phi(N), d and the CRT exponents

3 proc: store the key
Store every data in a PEM file and store the file into a folder

4..N proc: generate prime factors
Every other processus are dedicated to the prime factors generation

"""

end_program = False

def construct_key_pairs():
    while end_program == False:
        pass

def store_key():
    while end_program == False:
        pass

def clock(end_time: tuple):
    print (time.struct_time.tm_hour)

def keypairs_engine(time: tuple, pub_exp: int, nBits: int):
    if nBits < 2048:
        raise ValueError(("Incorrect key length. nBits must be equal or greater than 2048"))
    
    elif pub_exp%2 == 0 or not pow_fast(2, 16) <= pub_exp <= pow_fast(2, 256):
        raise ValueError("Incorrect puclic exponent. e must be odd and in the range [2^16, 2^256]")
    pBits = nBits//2

    processus = []
    processus.append(Process(target=clock, args=(time)))

