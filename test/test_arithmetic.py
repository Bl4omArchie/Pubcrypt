from pubcrypt.number import util

from random import randint
import math



def test_gcd():
    num_iter = 1000

    try:
        for _ in range(num_iter):
            a = randint(pow(2, 127), pow(2, 128))
            b = randint(pow(2, 127), pow(2, 128))
            assert(math.gcd(a, b) == util.gcd(a, b))
    except:
        raise (f"[!] FAILURE at num_iter = {num_iter}: a = {a}, b = {b}")
    print ("[*] TEST: 100% passed")

def test_invmod():
    num_iter = 1000

    try:
        for _ in range(num_iter):
            a = randint(pow(2, 127), pow(2, 128))
            b = randint(pow(2, 127), pow(2, 128))
            assert(pow(a, -1, b) == util.invmod(a, b))
    except:
        raise (f"[!] FAILURE at num_iter = {num_iter}: a = {a}, b = {b}")
    print ("[*] TEST: 100% passed")


def test_perfect_square():
    pass

def test_lcm():
    pass

def test_fast_exp_mod():
    num_iter = 1000

    try:
        for _ in range(num_iter):
            a = randint(pow(2, 127), pow(2, 128))
            b = randint(pow(2, 63), pow(2, 64))
            m  = randint(pow(2, 127), pow(2, 128))
            assert(pow(a, b, m) == util.fast_exp_mod(a, b, m))
    except:
        raise (f"[!] FAILURE at num_iter = {num_iter}: a = {a}, b = {b}")
    print ("[*] TEST: 100% passed")


def test_isqrt():
    pass


def run_all_tests():
    pass