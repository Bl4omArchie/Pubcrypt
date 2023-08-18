from pubcrypt.cryptosystem.rsa import generate, prime_recovery
from pubcrypt.number.primality import get_prime_factor
from benchmark.plotting import *
from benchmark.profiler import *


def plotting_sample():
    obj = GraphVisualization("Function generate")
    obj.measure_execution_time(1, generate, 2048)
    obj.plot_data(["green"], ["generate()"], show_stats=False, show_regression=True)

def profile_sample():
    obj = EffiencyProfile(get_prime_factor)
    obj.create_profile(1024, 65537)
    obj.read_profile()

if __name__ == "__main__":
    plotting_sample()