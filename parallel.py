import random
import multiprocessing

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Write n - 1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

def generate_and_test(start, end):
    prime_candidate = None
    for _ in range(start, end):
        num = random.randint(2**63, 2**64 - 1)  # Adjust range as needed
        if miller_rabin(num):
            prime_candidate = num
            break
    return prime_candidate

def main():
    num_threads = multiprocessing.cpu_count()  # Number of parallel threads
    pool = multiprocessing.Pool(processes=num_threads)
    
    chunk_size = 1000  # Number of numbers to generate and test per thread
    ranges = [(i, i + chunk_size) for i in range(0, num_threads * chunk_size, chunk_size)]
    
    prime_count = 0
    prime_numbers = []
    
    for prime_candidate in pool.starmap(generate_and_test, ranges):
        if prime_candidate is not None:
            prime_numbers.append(prime_candidate)
            prime_count += 1
            
            if prime_count >= 2:
                pool.terminate()
                pool.join()
                return prime_numbers[0], prime_numbers[1]
    
    print("No two prime numbers found.")

if __name__ == "__main__":
    print (main())
