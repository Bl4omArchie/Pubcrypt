from pubcrypt.cryptosystem.rsa import generate
from pubcrypt.parallel.rsa_thread import generate_multi_keypair
from pubcrypt.scheme.oaep import *


def oaep_test():
    n, e, d = generate(2048)
    plaintext = b"Hello, RSA OAEP!"
    ciphertext = rsa_oaep_encrypt(plaintext, n, e)
    #decrypted_text = rsa_oaep_decrypt(ciphertext, n, d)

    print("Original plaintext:", plaintext.decode('utf-8'))
    #print("Decrypted plaintext:", decrypted_text.decode('utf-8'))


def parallel_test():
    num_keys = 100
    num_proc = 2
    nBits = 2048   

    key_pairs = generate_multi_keypair(num_keys, num_proc, nBits)
    for i, (n, e, d) in enumerate(key_pairs, start=1):
        print(f"Key Pair {i} - n: {n}, e: {e}, d: {d}")

if __name__ == "__main__":
    parallel_test()