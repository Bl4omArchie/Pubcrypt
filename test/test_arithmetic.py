from pubcrypt.number import util
from random import randint
import math


num_iter = 500


def test_gcd():
    try:
        for i in range(num_iter):
            a = randint(pow(2, 127), pow(2, 128))
            b = randint(pow(2, 127), pow(2, 128))
            assert(math.gcd(a, b) == util.gcd(a, b))
    except:
        raise (f"[!] FAILURE at num_iter = {i}: a = {a}, b = {b}")
    print ("[*] GCD test: 100% passed")


def test_invmod():
    try:
        for i in range(num_iter):
            a = randint(pow(2, 127), pow(2, 128))
            b = randint(pow(2, 127), pow(2, 128))
            assert(pow(a, -1, b) == util.invmod(a, b))
    except:
        print (f"[!] FAILURE at num_iter = {i}: a = {a}, b = {b}")
        raise ValueError()
    print ("[*] Modular inverse test: 100% passed")


def test_karatsuba():
    try:
        for i in range(num_iter):
            a = randint(pow(2, 127), pow(2, 128))
            b = randint(pow(2, 127), pow(2, 128))
            assert(a*b == util.karatsuba(a, b))
    except:
        raise (f"[!] FAILURE at num_iter = {i}: a = {a}, b = {b}")
    print ("[*] Karatsuba test: 100% passed")


def test_perfect_square():
    pass

def test_lcm():
    pass

def test_fast_exp_mod():
    try:
        for i in range(num_iter):
            a = randint(pow(2, 127), pow(2, 128))
            b = randint(pow(2, 63), pow(2, 64))
            m  = randint(pow(2, 127), pow(2, 128))
            assert(pow(a, b, m) == util.fast_exp_mod(a, b, m))
    except:
        raise (f"[!] FAILURE at num_iter = {i}: a = {a}, b = {b}")
    print ("[*] modular exponentiation: 100% passed")


def test_isqrt():
    pass


def run_all_tests():
    test_gcd()
    #test_invmod()
    test_karatsuba()
    test_perfect_square()
    test_lcm()
    test_fast_exp_mod()
    test_isqrt()