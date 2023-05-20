import multiprocessing

from pubcrypt.number.primality import get_prime_factor_multi

def generate_keypair():
    prime_queue = multiprocessing.Queue()

    # Start the prime generation processes
    num_processes = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=get_prime_factor_multi, args=(1024, 65537, prime_queue,))
        process.daemon = True
        process.start()
        processes.append(process)

    # Collect prime factors
    prime_factors = []
    while len(prime_factors) < 2:
        prime = prime_queue.get()
        prime_factors.append(prime)

    # Wait for all processes to finish
    for process in processes:
        process.join()

    p, q = prime_factors
    print (p, q)


# Example usage
generate_keypair()