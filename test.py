from pubcrypt.cryptosystem.rsa import *
from pubcrypt.number.primality import *
from pubcrypt.number.util import *

from benchmark.gcd import *
from benchmark.pow import *
from benchmark.generate import *

import time



def simulation():
    """ This function verify that the module RSA work and give the execution time """

    try:
        #key size: 2048
        start1 = time.time()
        generate(2048)
        end1 = time.time()

        #key size: 4096
        start2 = time.time()
        generate(2048)
        end2 = time.time()

        #key size: 8196
        start3 = time.time()
        generate(2048)
        end3 = time.time()

        print ("-------- Generation ------")
        print (f"key = 2048: {end1-start1} ")
        print (f"key = 4096: {end2-start2} ")
        print (f"key = 8196: {end3-start3} ")
        print ("--------------------------")
    except:
        print ("[!] generation() has failed")



if __name__ == "__main__":
    simulation()