from random import randint
import time


min = pow(2, 511)
max = pow(2, 512)
mod = pow(2, 2048)


def get_time_fast_expo(n):
    result_old = []
    result_new = []
    python = []

    for _ in range(n):
        start_time = time.time()
        pow_mod(randint(min, max), 65537, randint(mod, mod))
        result_old.append(time.time() - start_time)

    for _ in range(n):
        start_time = time.time()
        pow_fast(randint(min, max), 65537, randint(mod, mod))
        result_new.append(time.time() - start_time)

    for _ in range(n):
        start_time = time.time()
        pow(randint(min, max), 65537, randint(mod, mod))
        python.append(time.time() - start_time)
    return result_old, result_new, python


def pow_fast(b, e, m=None):
    result = 1
    while e > 0:
        if e & 1:
            result *= b
            if m:
                result %= m
        b *= b
        if m:
            b %= m
        e >>= 1

    if m:
        result %= m
    return result


def pow_mod(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number