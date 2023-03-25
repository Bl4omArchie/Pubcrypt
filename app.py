from pubcrypt.cryptosystem.rsa import *
import argparse


def generate_keypair(nBits, e=65537):
    n, e, d = generate(nBits, e)
    print (f"n = {n}\ne = {e}\nd = {d}")

def encrypt(m, e, n):
    c = primitive_exp(m, e, n)
    print (f"C = {c}")

def decrypt(c, d, n):
    m = primitive_exp(c, d, n)
    print (f"M = {m}")

def recover_prime_factor(n, e, d):
    p, q = recover_prime_factor(n, e, d)
    print (f"p = {p}\nq = {q}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Call function from pubcrypt module')

    parser.add_argument('-g', type=int, help='Generate an RSA keypair. Indicate the bits size as an argument')
    parser.add_argument('-enc', type=int, help='encryption your data')
    parser.add_argument('-dec', type=int, help='decrypt your data')
    parser.add_argument('-r', action='store', help='recover your primes factor')

    parser.add_argument('-e', type=int, help='Public exponent. By default: e=65537')
    parser.add_argument('-n', type=int, help='Public modulus')
    parser.add_argument('-d', type=int, help='Private exponent')


    args = parser.parse_args()

    if args.g:
        try:
            if args.e == None:
                args.e = 65537
            generate_keypair(args.g, args.e)
        except:
            print ("Error: missing arguments '-e'")

    elif args.enc:
        try:
            encrypt(args.enc, args.e, args.n)
        except:
            print ("Error: missing arguments '-e' and '-n'")

    elif args.dec:
        try:
            decrypt(args.dec, args.d, args.n)
        except:
            print ("Error: missing arguments '-d' and '-n'")

    elif args.r:
        try:
            recover_prime_factor(args.n, args.e, args.d)
        except:
            print ("Error: missing arguments '-n', '-e' and '-d'")