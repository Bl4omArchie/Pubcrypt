from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.primality import *
from pubcrypt.number.util import *


"""
This test verify that everything work correcly. You can call every functions you want below.
"""


def launch_test():
    """ Launch this script to see if everything in pubcrypt module is working """
    try:
        n, e, d = generate(2048, e=65537)
        prime_recovery(n, e, d)
        get_prime_factor(1024, 65537)
        
    except:
        ValueError("Test failed")


if __name__ == "__main__":
    launch_test()