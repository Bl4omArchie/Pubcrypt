from pubcrypt.number import arithmetic
import gmpy2


class ArithmeticLib:
    def gcd(self, a, b):
        raise NotImplementedError
    
    def invmod(self, a, m):
        raise NotImplementedError
    
    def isqrt(self, n):
        raise NotImplementedError
    
    def exp(self, base, exp):
        raise NotImplementedError

    def lcm(self, x, y):
        raise NotImplementedError
    
    def powmod(self, base, exp, mod):
        raise NotImplementedError
    
    def karatsuba(self, x, y):
        raise NotImplementedError

    def integer(self):
        raise NotImplementedError

    def random_number(self):
        raise NotImplementedError

class PAL(ArithmeticLib):
    """ Pubcrypt Arithmetic library """
    def gcd(self, a, b):
        return arithmetic.gcd(a, b)
    
    def invmod(self, a, m):
        return arithmetic.invmod(a, m)
    
    def isqrt(self, n):
        return arithmetic.isqrt(n)
    
    def exp(self, base, exp):
        return pow(base, exp)

    def lcm(self, x, y):
        return arithmetic.lcm(x, y)
    
    def powmod(self, base, exp, mod):
        return arithmetic.fast_exp_mod(base, exp, mod)
    
    def karatsuba(self, x, y):
        return arithmetic.karatsuba(x, y)

    def integer(self):
        return int()

    def random_number(self, n):
        return random.getrandbits(n)



class GMP(ArithmeticLib):
    def gcd(self, a, b):
        return gmpy2.gcd(a, b)
    
    def invmod(self, a, m):
        return gmpy2.invert(a, m)
    
    def isqrt(self, n):
        return gmpy2.isqrt(n)
    
    def exp(self, base, exp):
        return pow(base, exp)

    def lcm(self, x, y):
        return gmpy2.lcm(x, y)
    
    def powmod(self, base, exp, mod):
        return pow(base, exp, mod)
    
    def karatsuba(self, x, y):
        raise ValueError("Karatsuba not supported by GMP")

    def integer(self):
        return mpz(0)

    def random_number(self, n):
        return gmpy2.mpz_random(gmpy2.random_state(), n)