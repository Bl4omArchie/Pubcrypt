import matplotlib.pyplot as plt
import numpy as np

size = (10, 8)


def make_simple_plot(array, title, label, color):
    fig, ax = plt.subplots(1, figsize=size)
    fig.suptitle(title, fontsize=15)
    plt.plot(np.linspace(1, len(array), len(array)), array, color=color, label=label)

    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.savefig("./benchmark/picture/"+title+".png")