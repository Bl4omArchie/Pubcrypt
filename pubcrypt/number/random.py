from random import randrange
from math import ceil


def RBG(nBits):
    return int_to_bytes(randrange(pow(2, nBits-1)+1, pow(2, nBits)-1))

def RNG(nBits):
    return randrange(pow(2, nBits-1)+1, pow(2, nBits)-1)


def int_to_bytes(x: int) :
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def bytes_to_int(xbytes: bytes) :
    return int.from_bytes(xbytes, 'big')


def MGF(seed, mask_len, hash_len):
    if mask_len > pow(2, 32): raise ValueError("Mask too long")

    T = ""
    for i in range(ceil(mask_len, hash_len)-1):
        