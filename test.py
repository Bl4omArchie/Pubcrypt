from benchmark.generate_bench import get_time
from benchmark.graph import make_simple_plot


def simulation():
    """ This function verify that the module RSA work and give the execution time """
    time = get_time(10, 2048)
    make_simple_plot(time, "Generate function with old MillerRabin", "generate()", "red")


if __name__ == "__main__":
    simulation()