from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.primality import *
from pubcrypt.number.util import *

from pubcrypt.scheme.oaep import rsa_oaep_encrypt

from benchmark.gcd import *
from benchmark.pow import *
from benchmark.generate import *



def launch_test():
    """ Launch this script to see if everything in pubcrypt module is working """
    try:
        n, e, d = generate(2048, e=65537)
        prime_recovery(n, e, d)
        get_prime_factor(1024, 65537)
        
    except:
        print ("[!] KeyPair generation failed")


def convert_test():
    """ Verify that the int_to_string and string_to_int work well """
    try:
        n = 65537
        string = int_to_string(n, ceil(n.bit_length()/8), "little")
        n2 = string_to_int(string, "little")

        print (f"n: {n} | type: {type(n)}")
        print (f"string: {string} - type: {type(string)}")
        print (f"n2: {n2} | type: {type(n2)}")
    except:
        print ("[!] Convert test failed")


def oaep_scheme_test():
    try:
        n, e, d = generate(2048, e=65537)
        m = b"verify the oaep scheme"
        rsa_oaep_encrypt(m, e, n)
    except:
        print ("[!] OAEP scheme encryption failed")



if __name__ == "__main__":
    launch_test()
    convert_test()
    oaep_scheme_test()