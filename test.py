from test import test_arithmetic

from pubcrypt.parallel.rsa_thread import *
from pubcrypt.cryptosystem.rsa import generate


if __name__ == "__main__":
    print(generate(2048))
    #test_arithmetic.run_all_tests()