from pubcrypt.cryptosystem.rsa import generate
import matplotlib.pyplot as plt
from random import randrange
import time


def bench_generate(n, nBits, e=65537):
    """ generate n times a nBits bit size key """
    for _ in range(n):
        generate(nBits)

def launch_generate_bench(n, nBits):
    plot_x = []
    plot_y = []

    fig, ax = plt.subplots(1, figsize=(25, 15))
    fig.suptitle('Benchmark Keypair generation', fontsize=15)

    for _ in range(1, n+1):
        start_time = time.time()
        generate(nBits)
        plot_y.append(time.time() - start_time)
        plot_x.append(_)

    plt.plot(plot_x, plot_y, color="green", label="generate()")

    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.savefig("benchmark/graph/benchmark_generate")