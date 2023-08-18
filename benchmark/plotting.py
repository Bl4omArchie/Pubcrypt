import matplotlib.pyplot as plt
import numpy as np
import time


class GraphVisualization:
    def __init__(self, title, size=(10, 8)) -> None:
        self.title = title
        self.size = size
        self.execution_times = []
        self.path = "benchmark/graph/"


    def measure_execution_time(self, n, func, *args, **kwargs):
        func_times = []
        for _ in range(n):
            start = time.time()
            func(*args, **kwargs)
            func_times.append("{:.10f}".format(time.time() - start))
        self.execution_times.append(func_times)


    def plot_data(self, colors, labels, graph_type='lines', show_stats=False, show_regression=False):
        if len(self.execution_times) != len(colors) or len(self.execution_times) != len(labels):
            raise ValueError("Lengths of execution_times, colors, and labels should be the same.")
        
        if graph_type not in ['lines', 'scatter']:
            raise ValueError("Invalid graph_type. Choose from 'lines' or 'scatter'")

        plt.figure(figsize=self.size)
        for i, data in enumerate(self.execution_times):
            if graph_type == 'lines':
                plt.plot(data, color=colors[i], label=labels[i])
            elif graph_type == 'scatter':
                plt.scatter(range(len(data)), data, color=colors[i], marker='o', label=f"{labels[i]} Points")

            if show_stats:
                mean = np.mean(data)
                max_val = max(data)
                min_val = min(data)
                plt.text(len(data) - 1.5, mean, f"Mean: {mean:.2f}")
                plt.text(len(data) - 1.5, max_val, f"Max: {max_val}")
                plt.text(len(data) - 1.5, min_val, f"Min: {min_val}")

            if show_regression:
                x_vals = np.arange(len(data))
                slope, intercept = np.polyfit(x_vals, data, 1)
                regression_line = intercept + slope * x_vals
                plt.plot(x_vals, regression_line, linestyle='dashed', color=colors[i])

        plt.title(self.title)
        plt.xlabel("Nombre d'exécution")
        plt.ylabel("Durée en seconde")
        plt.legend()
        plt.grid(True)
        plt.savefig(self.path+self.title)