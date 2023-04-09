import matplotlib.pyplot as plt
from random import getrandbits, randrange
import time


def binary_pow(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def launch_pow_bench(n):
    plot_x = [[], [], []]
    plot_y = [[], [], []]

    fig, ax = plt.subplots(1, figsize=(25, 15))
    fig.suptitle('Benchmark POW', fontsize=15)

    for _ in range(1, n+1):
        a = getrandbits(1024)
        b = randrange(pow(2, 16), pow(2, 256))
        c = getrandbits(2048)

        start_time = time.time()
        pow(a, b, c)
        plot_y[0].append(time.time() - start_time)
        plot_x[0].append(_)

        start_time = time.time()
        binary_pow(a, b, c)
        plot_y[1].append(time.time() - start_time)
        plot_x[1].append(_)

    plt.plot(plot_x[0], plot_y[0], color="green", label="python_pow()")
    plt.plot(plot_x[1], plot_y[1], color="blue", label="binary_gcd()")
    #plt.plot(plot_x[2], plot_y[2], color="red", label="binary_gcd_assembly_improve()")

    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.savefig("benchmark/graph/benchmark_pow")