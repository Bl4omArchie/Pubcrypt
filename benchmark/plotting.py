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
            func_times.append(time.time() - start)
        self.execution_times.append(func_times)


    def plot_data(self, colors, labels, graph_type='lines', show_stats=False, show_regression=False):
        if len(self.execution_times) != len(colors) or len(self.execution_times) != len(labels):
            raise ValueError("Lengths of execution_times, colors, and labels should be the same.")
        
        if graph_type not in ['lines', 'scatter']:
            raise ValueError("Invalid graph_type. Choose from 'lines' or 'scatter'")

        plt.figure(figsize=self.size)
        for i in range(len(self.execution_times)):
            data_chunck_size = len(self.execution_times[i])
            if graph_type == 'lines':
                plt.plot(np.linspace(0, data_chunck_size, data_chunck_size), self.execution_times[i], color=colors[i], label=labels[i])


        plt.title(self.title)
        plt.xlabel('Test Iteration')
        plt.ylabel('Elapsed Time (seconds)')
        plt.legend()
        plt.grid(True)
        plt.savefig(self.path+self.title)