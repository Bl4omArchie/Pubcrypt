import time
import psutil
import os
import functools
from math import *


def resource_monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Measure start CPU and memory usage
        process = psutil.Process(os.getpid())
        start_cpu_times = process.cpu_times()
        start_memory_info = process.memory_info()
        start_time = time.time()

        result = func(*args, **kwargs)
        
        end_time = time.time()
        end_cpu_times = process.cpu_times()
        end_memory_info = process.memory_info()

        # Calculate resource usage
        elapsed_time = end_time - start_time
        user_cpu_time = end_cpu_times.user - start_cpu_times.user
        system_cpu_time = end_cpu_times.system - start_cpu_times.system
        memory_used = end_memory_info.rss - start_memory_info.rss

        # Print resource usage
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds")
        print(f"User CPU time: {user_cpu_time:.4f} seconds")
        print(f"System CPU time: {system_cpu_time:.4f} seconds")
        print(f"Memory used: {memory_used / 1024 / 1024:.4f} MB")

        return result

    return wrapper


def get_length(num):
    length = 0
    while num:
        length += 1
        num >>= 1
    return length


# Example usage
@resource_monitor
def powmod(b, e, m):
    result = 1
    b %= m  
    while e > 0:
        if e & 1:
            result = (result * b) % m
        b = (b * b) % m
        e >>= 1
    return result % m

# Call the example function to see the resource usage
print (powmod(2**1024, 0x234FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF, 2**2048))