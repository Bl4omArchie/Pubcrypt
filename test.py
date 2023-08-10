from benchmark.generate_bench import get_time
from benchmark.graph import make_simple_plot


def simulation():
    time = get_time(50, 2048)
    make_simple_plot(time, "Generate function", "generate()", "green")


if __name__ == "__main__":
    simulation()