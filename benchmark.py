from pubcrypt.cryptosystem.rsa import generate, prime_recovery
from pubcrypt.number.primality import get_prime_factor
from benchmark.plotting import *
from benchmark.profiler import *


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
    obj.measure_execution_time(150, generate, 2048)
    obj.plot_data(["green"], ["generate()"], show_stats=True)

def profile_sample():
    obj = EffiencyProfile(get_prime_factor)
    obj.create_profile(1024, 65537)
    obj.read_profile()

if __name__ == "__main__":
    plotting_sample()