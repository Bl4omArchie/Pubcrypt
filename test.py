from pubcrypt.cryptosystem.rsa import generate
from pubcrypt.scheme.oaep import *


if __name__ == "__main__":
    n, e, d = generate(2048)
    plaintext = b"Hello, RSA OAEP!"
    ciphertext = rsa_oaep_encrypt(plaintext, n, e)
    decrypted_text = rsa_oaep_decrypt(ciphertext, n, d)

    print("Original plaintext:", plaintext.decode('utf-8'))
    print("Decrypted plaintext:", decrypted_text.decode('utf-8'))