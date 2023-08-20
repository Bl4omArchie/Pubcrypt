import matplotlib.pyplot as plt
import numpy as np
import time


class GraphVisualization:
    def __init__(self, title, size=(15, 13)) -> None:
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


    def plot_data(self, colors, labels, graph_type='lines', show_stats=False):
        if len(self.execution_times) != len(colors) or len(self.execution_times) != len(labels):
            raise ValueError("Lengths of execution_times, colors, and labels should be the same.")
        
        if graph_type not in ['lines', 'scatter']:
            raise ValueError("Invalid graph_type. Choose from 'lines' or 'scatter'")

        plt.figure(figsize=self.size)
        for i in range(len(self.execution_times)):
            data_chunk_size = len(self.execution_times[i])
            if graph_type == 'lines':
                plt.plot(np.linspace(0, data_chunk_size, data_chunk_size), self.execution_times[i], color=colors[i], label=labels[i])

            if show_stats:
                min_value = np.min(self.execution_times[i])
                max_value = np.max(self.execution_times[i])
                mean_value = np.mean(self.execution_times[i])
                plt.text(data_chunk_size, min_value, f"Min: {min_value:.10f}", verticalalignment='top', horizontalalignment='left')
                plt.text(data_chunk_size, max_value, f"Max: {max_value:.10f}", verticalalignment='top', horizontalalignment='right')
                plt.text(data_chunk_size, mean_value, f"Mean: {mean_value:.10f}", verticalalignment='top', horizontalalignment='right')

        plt.title(self.title)
        plt.xlabel('Test Iteration')
        plt.ylabel('Elapsed Time (seconds)')
        plt.legend()
        plt.grid(True)
        plt.savefig(self.path + self.title)