from benchmark.generate import get_time
from benchmark.conversion import get_time_converting
from benchmark.isqrt import get_time_isqrt
from benchmark.fast_expo import get_time_fast_expo
from benchmark.gcd import get_time_gcd

from benchmark.graph import *


def simulation():
    time = get_time(50, 2048)
    make_simple_plot(time, "generate() with new binary algorithm", "generate()", "red")

    time1, time2 = get_time_converting(1000)
    make_n_plot("plot", (time1, time2), "Comparing conversion integer to binary", ("original", "new"), ("red", "green"))

    time1, time2 = get_time_isqrt(1000)
    make_n_plot("plot", (time1, time2), "Comparing isqrt", ("original", "new"), ("red", "green"))

    time1, time2, time3 = get_time_fast_expo(100)
    make_n_plot("point", (time1, time2, time3), "Comparing several fast modular exponentiation function", ("old", "new", "python"), ("red", "green", "purple"))

    time1, time2, time3 = get_time_gcd(100)
    make_n_plot("point", (time1, time2, time3), "Comparing several gcd function", ("old", "new", "python"), ("red", "green", "purple"))
    

if __name__ == "__main__":
    simulation()