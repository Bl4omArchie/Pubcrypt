from pubcrypt.number.primality import get_prime_factor
import cProfile, random, os, sys


"""
python3 app.py -b generate 2048 50

python3 app.py -plot generate scatter

"""

mini = pow(2, 1024)
maxi = pow(2, 1025)

def execute1(n):
    for i in range(n):
        random.randint(mini, maxi-1)

def execute2(n):
    for i in range(n):
        random.randrange(mini, maxi-1)

def execute3(n):
    for i in range(n):
        os.urandom(1024)

if __name__ == "__main__":
    cProfile.run('get_prime_factor(1024, 65537)')