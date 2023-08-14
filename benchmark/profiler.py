import pstats, cProfile
from pstats import SortKey
from pubcrypt.cryptosystem.rsa import generate, prime_recovery
from pubcrypt.number.primality import *

path = "profile/"
sufix = ".profile" 

#List of the function that need a profile
feature = {1: "generate", 2: "prime_recovery", 3: "get_prime_factor", 4: "miller_rabin"}


def create_profile(fnum, profile_name):
    profile = cProfile.run(f"{feature[fnum]}()")

    with open(path+profile_name+sufix, "w") as fp:
        fp.write(profile)


def read_profile(profile_name):
    p = pstats.Stats(path+profile_name+sufix)
    return p.strip_dirs().sort_stats(-1).print_stats()