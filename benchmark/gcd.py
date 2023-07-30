import time, math


a = pow(2, 1023)
b = pow(2, 1024)


def get_time_gcd(n):
    result_old = []
    result_new = []
    python = []

    for _ in range(n):
        start_time = time.time()
        gcd_old(a, b)
        result_old.append(time.time() - start_time)

    for _ in range(n):
        start_time = time.time()
        gcd_binary(a, b)
        result_new.append(time.time() - start_time)

    for _ in range(n):
        start_time = time.time()
        math.gcd(a, b)
        python.append(time.time() - start_time)
    return result_old, result_new, python


def gcd_old(x, y):
    r = [x, y]
    i = 1
    while r[i] >= 0:
        i += 1
        r.append(r[i-2] % r[i-1])

        if r[i] == 0:
            return r[i-1]

def gcd_binary(x, y):
    if x == 0:
        return y
    if y == 0:
        return x

    x_rightmost = x & -x
    y_rightmost = y & -y

    while x_rightmost != y_rightmost:
        if x_rightmost > y_rightmost:
            x_rightmost >>= 1
        else:
            y_rightmost >>= 1

    return x_rightmost