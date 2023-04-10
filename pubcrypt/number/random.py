from random import getrandbits
from math import ceil


def RBG(nBits):
    """ return a byte string of nBits"""
    return int_to_string(getrandbits(nBits), ceil(nBits/8))

def RNG(nBits):
    """ return an integer of nBits"""
    return getrandbits(nBits)


def int_to_string(x, xLen, order="big"):
    """
    Converts a nonnegative integer to an octet string (bytes) of a specified length

    params:
        x: the integer
        xLen: len of the output
        order: big-endian (big) or little-endian (little). By default I use big-endian
    """
    result = bytearray(xLen)

    for i in range(xLen):
        byte = x & 0xff
        result[xLen-i-1] = byte
        x >>= 8

    if order == "little": 
        result = result[::-1]
    return bytes(result)


def string_to_int(x, order="big"):
    """
    Converts an octet string (bytes) to a integer

    params:
        x: the octet string
    """
    if order == "little":
        x = x[::-1]
    n = 0
    for byte in x:
        n <<= 8
        n += byte
    return n


def MGF(seed, mask_len, hash_len):
    if mask_len > pow(2, 32): raise ValueError("Mask too long")