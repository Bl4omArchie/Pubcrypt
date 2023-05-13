from pubcrypt.number.util import int_to_string
from random import getrandbits
from math import ceil


def RBG(nBits):
    """ return a byte string of nBits"""
    return int_to_string(getrandbits(nBits), ceil(nBits/8))

def RNG(nBits):
    """ return an integer of nBits"""
    return getrandbits(nBits)