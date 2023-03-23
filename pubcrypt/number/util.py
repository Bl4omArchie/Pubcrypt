from math import floor, log2, ceil


def invmod(z, a):
    if not z < a:
        z, a = a, z

    i, j = a, z
    y1, y2 = 1, 0

    while True:
        q = i//j
        r = i - (j*q)
        y = y2 - (y1*q)
        i, j = j, r
        y2, y1 = y1,y

        if j>0:
            continue

        else:
            break

    return y2%a


def gcd(x, y):
    r = [x, y]
    i = 1
    while r[i] >= 0:
        i += 1
        r.append(r[i-2] % r[i-1])

        if r[i] == 0:
            return r[i-1]

def lcm(x, y):
    return (x*y) // gcd(x, y)


def pow_mod(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def isqrt (x):
    """ Credit: https://rosettacode.org/wiki/Isqrt_(integer_square_root)_of_X#Python """
    q = 1
    while q <= x : 
        q *= 4

    z, r = x, 0
    while q > 1 :
        q //= 4
        t, r = z-r-q, r//2
        if t >= 0 :
            z, r = t, r+q
    return r 

def perfect_square(c):
    n = floor(log2(abs(c))) + 1
    m = ceil(n/2)
    x = pow(2, m) - pow(2, m-1)

    while True:
        x = (pow(x, 2)+c)/(2*x)

        if pow(x, 2) < pow(2, m)+c:
            break

    return c == pow(floor(x), 2)


def int_to_bin(n, iter="big"):
    result = ""
    while n > 0:
        if n%2 == 0:
            result += "0"
        else:
            result += "1"
        n = n //2
        
    if iter == "little":
        return result
    else:
        return result[::-1]