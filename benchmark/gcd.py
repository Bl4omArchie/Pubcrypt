import matplotlib.pyplot as plt
from random import randrange
from math import gcd
import time


def binary_gcd(x, y):
    r = [x, y]
    i = 1
    while r[i] >= 0:
        i += 1
        r.append(r[i-2] % r[i-1])

        if r[i] == 0:
            return r[i-1]
        
def binary_gcd_assembly_improve(a, b):
    if a == 0: return b
    if b == 0: return a

    az = a
    bz = b
    shift = min(az, bz)
    b >>= bz
    
    while a != 0:
        a >>= az
        diff = b - a
        az = diff
        b = min(a, b)
        a = abs(diff)
    
    return b << shift

def launch_gcd_bench(n):
    plot_x = [[], [], []]
    plot_y = [[], [], []]

    fig, ax = plt.subplots(1, figsize=(25, 15))
    fig.suptitle('Benchmark GCD', fontsize=15)

    for _ in range(1, n+1):
        a = randrange(pow(2, 16), pow(2, 256))
        b = randrange(pow(2, 16), pow(2, 256))

        start_time = time.time()
        gcd(a, b)
        plot_y[0].append(time.time() - start_time)
        plot_x[0].append(_)

        start_time = time.time()
        binary_gcd(a, b)
        plot_y[1].append(time.time() - start_time)
        plot_x[1].append(_)

        start_time = time.time()
        binary_gcd_assembly_improve(a, b)
        plot_y[2].append(time.time() - start_time)
        plot_x[2].append(_)

    plt.plot(plot_x[0], plot_y[0], color="green", label="python_gcd()")
    plt.plot(plot_x[1], plot_y[1], color="blue", label="binary_gcd()")
    plt.plot(plot_x[2], plot_y[2], color="red", label="binary_gcd_assembly_improve()")

    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.savefig("benchmark/graph/benchmark_gcd")