from pubcrypt.cryptosystem.rsa_GMP import *
from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.primality import *
from pubcrypt.number.util import *
from benchmark.plotting import *
from benchmark.profiler import *

import random, math, os


"""
This benchmark intend to evaluate the effiency of Pubcrypt's function
With only two simples class: GraphVisualization and EffiencyProfile, I have access to a good overview of the performance.

- GraphVisualization allow me to generate a graph that plot the times of execution for one or severals function.
- EffiencyProfile generate a profile with the library cProfile which is specialised in examining function in details. It give me information about witch modules are called in the function, how many I have been calling them and the final generation time.
This evaluation is more accurated for huge function that used many external packages.

There is two examples:
"""


def plotting_sample():
    obj = GraphVisualization("Function generate")
    obj.measure_execution_time(100, generate, 2048)
    obj.plot_data(["green"], ["generate()"], show_stats=True)

def profile_sample():
    obj = EffiencyProfile(generate)
    obj.create_profile(2048)
    obj.read_profile()

def gcd_test():
    #Comparison between my implementation of gcd and python's built-in function
    n = 5000
    obj = GraphVisualization("GCD comparison")
    obj.measure_execution_time(n, gcd, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
    obj.measure_execution_time(n, math.gcd, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
    obj.plot_data(["green", "red"], ["gcd()", "python gcd()"], show_stats=True)

def pow_test():
    #Comparison between my implementation of fast exponentiation (pow_fast) and python's built-in function
    n = 1000
    obj = GraphVisualization("Fast exponentiation comparison")
    obj.measure_execution_time(n, pow, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
    obj.measure_execution_time(n, pow_fast, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
    obj.plot_data(["green", "red"], ["python pow()", "pow_fast()"], show_stats=True)

def rng_test():
    #Comparison between different way of generating a random number
    n = 1000
    obj = GraphVisualization("RNG comparison")
    obj.measure_execution_time(n, random.getrandbits, 2048)
    obj.measure_execution_time(n, random.randint, 2**2048, 2**2049)
    obj.measure_execution_time(n, random.randrange, 2**2048, 2**2049)
    obj.measure_execution_time(n, os.urandom, 2048)
    obj.plot_data(["green", "red", "blue", "purple"], ["getrandbits()", "randint()", "randrange()", "urandom()"], show_stats=False)

def rsa_GMP_test():
    n = 100
    obj = GraphVisualization("RSA GMP generate function")
    obj.measure_execution_time(n, generate_gmp, 4096)
    obj.plot_data(["green"], ["generate_gmp()"], show_stats=True)

def decryption_using_crt():
    n = 250
    N, e, d = generate(2048)
    obj = GraphVisualization("CRT and primitive decryption")
    obj.measure_execution_time(n, crt_decrypt, random.randint(2**255, 2**256), N, e, d)
    obj.measure_execution_time(n, primitive_exp, random.randint(2**255, 2**256), d, N)
    obj.plot_data(["green", "red"], ["crt_decryption()", "decryption()"], show_stats=True)


if __name__ == "__main__":
    pow_test()