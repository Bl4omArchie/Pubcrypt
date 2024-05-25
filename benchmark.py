from pubcrypt.cryptosystem.rsa import *

from pubcrypt.number.primality import *
from pubcrypt.number.arithmetic import *
from pubcrypt.number.util import *

from pubcrypt.number.lib import PAL, GMP

from benchmark.plotting import *
from benchmark.profiler import *

import random, math, os


"""
This benchmark intend to evaluate the effiency of Pubcrypt's function
With only two simples class: GraphVisualization and EffiencyProfile, I have access to a good overview of the performance.

- GraphVisualization allow me to generate a graph that plot the times of execution for one or severals function.
- EffiencyProfile generate a profile with the library cProfile which is specialised in examining function in details. It give me information about witch modules are called in the function, how many I have been calling them and the final generation time.
This evaluation is more accurated for huge function that used many external packages.
"""

def generate_bench(library=PAL()):
    n = 10
    key_size = 2048
    obj = GraphVisualization("Function generate")
    obj.measure_execution_time(n, generate, key_size, library)
    obj.plot_data(["green"], ["generate()"], show_stats=True)

def gcd_bench():
    #Comparison between my implementation of gcd and python's built-in function
    n = 5000
    obj = GraphVisualization("GCD comparison")
    obj.measure_execution_time(n, gcd, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
    obj.measure_execution_time(n, math.gcd, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
    obj.plot_data(["green", "red"], ["gcd()", "python gcd()"], show_stats=True)

def pow_bench():
    #Comparison between my implementation of fast exponentiation (fast_exp_mod) and python's built-in function
    n = 500
    obj = GraphVisualization("Fast exponentiation comparison")
    obj.measure_execution_time(n, pow, random.randint(2**1024, 2**1025), 65337, random.randint(2**2048, 2**2049))
    obj.measure_execution_time(n, fast_exp_mod, random.randint(2**1024, 2**1025), 65537, random.randint(2**2048, 2**2049))
    obj.plot_data(["green", "red"], ["python pow()", "fast_exp_mod()"], show_stats=True)

    obj = GraphVisualization("Fast modular exp comparison")
    obj.measure_execution_time(n, pow, random.randint(2**1024, 2**1025), 65537, random.randint(2**2048, 2**2049))
    obj.measure_execution_time(n, fast_exp_mod, random.randint(2**1024, 2**1025), 65537, random.randint(2**2048, 2**2049))
    obj.plot_data(["green", "purple"], ["python pow", "fast_exp_mod"], show_stats=True)

def rng_bench():
    #Comparison between different way of generating a random number
    n = 500
    obj = GraphVisualization("RNG comparison")
    obj.measure_execution_time(n, random.getrandbits, 2048)
    obj.measure_execution_time(n, random.randint, 2**2048, 2**2049)
    obj.measure_execution_time(n, random.randrange, 2**2048, 2**2049)
    obj.measure_execution_time(n, os.urandom, 2048)
    obj.plot_data(["green", "red", "blue", "purple"], ["getrandbits()", "randint()", "randrange()", "urandom()"], show_stats=False)

def decryption_using_crt():
    n = 250
    N, e, d = generate(2048)
    obj = GraphVisualization("CRT and primitive decryption")
    obj.measure_execution_time(n, crt_decrypt, random.randint(2**255, 2**256), N, e, d)
    obj.measure_execution_time(n, primitive_exp, random.randint(2**255, 2**256), d, N)
    obj.plot_data(["green", "red"], ["crt_decryption()", "decryption()"], show_stats=True)


def invmod_bench():
    #Comparison between my implementation of invmod and the one from Crypto.Util.number module
    n = 5000
    obj = GraphVisualization("Invmod comparison")
    obj.measure_execution_time(n, invmod, random.randint(2**512, 2**1024), random.randint(2**1024, 2**2048))
    obj.measure_execution_time(n, inverse, random.randint(2**512, 2**1024), random.randint(2**1024, 2**2048))
    obj.plot_data(["green", "red"], ["invmod()", "number.invmod()"], show_stats=True)


def karatsuba_bench():
    n = 500
    obj = GraphVisualization("Karatsuba multiplication")
    obj.measure_execution_time(n, karatsuba, random.randint(2**1023, 2**1024), random.randint(2**1024, 2**2048))
    obj.measure_execution_time(n, karatsuba2, random.randint(2**1023, 2**1024), random.randint(2**1024, 2**2048))
    obj.plot_data(["green", "red"], ["karatsuba()", "karatsuba2()"], show_stats=True)


if __name__ == "__main__":
    generate_bench()