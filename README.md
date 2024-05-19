# Pubcrypt ~ RSA keypair generation

Pubcrypt is a personnal project that aim to implement in python public key cryptography. I'm doing this to train my coding skills and learn good programming practise.
See this repo as an experiment, I'm not aiming to make the "perfect" and most optmized implementation. I'm testing various algorithm and evaluating their efficiency (see benchmark folder). 


Table of contents:
- [Pubcrypt ~ RSA keypair generation](#pubcrypt--rsa-keypair-generation)
- [Roadmap](#roadmap)
- [Features](#features)
  - [RSA algorithm](#rsa-algorithm)
  - [Benchmark](#benchmark)
  - [RSA GMP](#rsa-gmp)
- [Author](#author)
- [References](#references)

# Roadmap

Actual todo-list:

- Improve tests
- OAEP scheme for encryption and decryption
- PSS scheme for signature
- CONTRIBUTING.md
- More cryptosystem ?


# Features 

## RSA algorithm

The first cryptosystem I implemented is RSA. I'm mainly focused on this one because I found it interesting with many side-algorithm to implement (scheme, CRT...).
You can find the main core of the algo in pubcrypt/cryptosystem/rsa.py and the primality test in pubcrypt/number.primality.py .

Try it yourself:

```py
from pubcrypt.cryptosystem import rsa

key = rsa.generate(2048)
print (f"N = {key[0]}, e = {key[1]}, d = {key[2]}")

```

## Benchmark

This benchmark intend to evaluate the effiency of Pubcrypt's function
With only two simples class: GraphVisualization and EffiencyProfile, I have access to a good overview of the performance.

- GraphVisualization allow me to generate a graph that plot the times of execution for one or severals function.
- EffiencyProfile generate a profile with the library cProfile which is specialised in examining function in details. It give me information about witch modules are called in the function, how many I have been calling them and the final generation time.
This evaluation is more accurated for huge function that used many external packages.

## RSA GMP

As I started implementing RSA cryptosystem in C with the GMP library, I was curious to see how much the python GMP library could be faster than mine.
So I implemented another RSA key pairs generator but with the gmpy2 module that you can find in both file: rsa_GMP.py and primality_GMP.py
A graph for the generation of 100 keys with this algorithm is available in the benchmark/graph folder named "RSA GMP generate function".**
The outcome is surrounding: my implementation is, from far, slower ! The python GMP implementation burst everything with a maximal generating time of 2.5 seconds. Still we can notice that the average time is 2.3 seconds while Pubcrypt is 2.4 seconds. 
As a conclusion GMP is more stable than my implementation but not "faster" because the minimal generating time is around 2.2 seconds while pubcrypt go down under the second (0.24s).  



# Author
You can contact me and see my work here:
- Blog: https://bl4omarchie.github.io/archX/
- Discord server: https://discord.com/invite/D2wGP62
- Twitter: https://twitter.com/Bl4om_Archie

# References
 - [NIST FIPS 186-4: Digital Signature Standard (DSS)](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.186-4.pdf)
 - [NIST SP 800-56Br2: Recommendation for Pair-Wise Key Establishment Using Integer Factorization Cryptography](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br2.pdf)
 - [PKCS #1 Version 2.2: RSA Cryptography Specifications draft-moriarty-pkcs1-01](https://datatracker.ietf.org/doc/pdf/draft-moriarty-pkcs1-01.pdf)
 - [Finding Large Primes for Public Key Cryptography](https://ghenshaw-work.medium.com/finding-large-primes-for-public-key-cryptography-9c5a5c0d32c4)
 - [RosettaCode](https://rosettacode.org/wiki/Rosetta_Code)
 - [Gmpy2 documentation](https://gmpy2.readthedocs.io/en/latest/index.html)