import time, cProfile, pstats


path = "benchmark/profiles/"
sufix = ".ep"

class EffiencyProfile:
    def __init__(self, func):
        self.func = func
        self.func_name = str(func)
        self.profile_file = path + f"{self.func_name}" + sufix

    def createe_profile(self, *args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        self.func(*args, **kwargs)
        profiler.disable()
        profiler.dump_stats(self.profile_file)

    def read_profile(self):
        stats = pstats.Stats(self.profile_file)
        stats.print_stats()