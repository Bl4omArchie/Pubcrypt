import matplotlib.pyplot as plt
import numpy as np


size = (18, 15)
path = "./benchmark/picture/"



def make_simple_plot(array, title, label, color):
    fig, ax = plt.subplots(1, figsize=size)
    fig.suptitle(title, fontsize=15)
    plt.plot(np.linspace(1, len(array), len(array)), array, color=color, label=label)

    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.savefig(path+title+".png")




def make_n_plot(type, arrays, title, labels, colors):
    size_data = []
    for data in arrays:
        size_data.append(len(data))

    fig, ax = plt.subplots(1, figsize=size)
    fig.suptitle(title, fontsize=15)

    for i in range(len(arrays)):
        if type == "plot":
            plt.plot(np.linspace(1, size_data[i], size_data[i]), arrays[i], color=colors[i], label=labels[i])
        elif type == "point":
            plt.scatter(np.linspace(1, size_data[i], size_data[i]), arrays[i], color=colors[i], label=labels[i])

    plt.xlabel('number of execution')
    plt.ylabel('execution time in second')

    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.savefig(path+title+".png")