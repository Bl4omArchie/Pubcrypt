import pstats, cProfile
from pstats import SortKey


path = "profile/"
sufix = ".profile" 



def create_profile(function, profile_name):
    cProfile.run(f"{function}()", path+profile_name+sufix)


def read_profile(profile_name):
    p = pstats.Stats(path+profile_name+sufix)
    p.strip_dirs().sort_stats(-1).print_stats()