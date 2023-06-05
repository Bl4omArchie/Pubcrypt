from pubcrypt.cryptosystem.rsa import generate
from pubcrypt.number.primality import miller_rabin
import matplotlib.pyplot as plt
import time


windows_size = (15, 13)
title1 = "Miller Rabin primality test"
title2 = "Keypair generation"
path = "benchmark/graph/"


def launch_miller_rabin_bench(n, nBits):
    plot_x = []
    plot_y = []

    fig, ax = plt.subplots(1, figsize=windows_size)
    fig.suptitle(title1, fontsize=15)

    for _ in range(1, n+1):
        start_time = time.time()
        miller_rabin(nBits, 5)
        plot_y.append(time.time() - start_time)
        plot_x.append(_)

    plt.plot(plot_x, plot_y, color="green", label="miller_rabin()")

    plt.legend(loc="upper right", title="Legend", frameon=False)
    #plt.savefig(path + "benchmark_miller_rabin")
    plt.show()



def launch_generate_bench(n, nBits):
    plot_x = []
    plot_y = []

    fig, ax = plt.subplots(1, figsize=windows_size)
    fig.suptitle(title2, fontsize=15)

    for _ in range(1, n+1):
        start_time = time.time()
        generate(nBits)
        plot_y.append(time.time() - start_time)
        plot_x.append(_)

    plt.plot(plot_x, plot_y, color="green", label="generate()")

    plt.legend(loc="upper right", title="Legend", frameon=False)
    #plt.savefig(path + "benchmark_generate")
    plt.show()