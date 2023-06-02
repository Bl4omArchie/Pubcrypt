import matplotlib.pyplot as plt
from random import randint



def generate_graph_plot(array_x, array_y, title, label):
    colors = ["blue", "green", "yellow", "black", "red", "purple", "pink", "orange"]
    scolors = len(colors)

    fig, ax = plt.subplots(1, figsize=(25, 15))
    fig.suptitle(title, fontsize=15)

    for i in range(len(array_x)):
        color = colors[randint(scolors)]
        colors.remove(color)
        plt.plot(array_x[i], array_y[i], color=color, label=label[i])

    plt.legend(loc="upper right", title="Legend", frameon=False)
    plt.show()