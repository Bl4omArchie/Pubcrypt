# Pubcrypt ~ RSA keypair generation

Pubcrypt is python library that aim to implement self-made cryptographic algorithms.
I first started this project for training myself with NIST's publication.
Actually Pubcrypt perform RSA keypairs generation, encryption, decryption, key recovery and more.

I'm looking to make this project open-source so everyone can contribute and implement more features. 


Table of contents:
- [Pubcrypt ~ RSA keypair generation](#pubcrypt--rsa-keypair-generation)
- [Tutorial](#tutorial)
  - [Installation](#installation)
  - [Command line](#command-line)
- [Roadmap](#roadmap)
- [Features](#features)
  - [Benchmark](#benchmark)
  - [RSA GMP](#rsa-gmp)
- [Author](#author)
- [References](#references)

#  Tutorial

## Installation
- Install the very last version: ```git clone https://github.com/Bl4omArchie/pubcrypt``` <br>
- Install the last stable version: https://github.com/Bl4omArchie/Pubcrypt/releases/tag/v1.5.2

Pubcrypt is self-made and do not required any depencies. It should work for python3.6 and more.

## Command line

With the app.py file, call directly your function from the command line:
``` 
usage: app.py [-h] [-g G] [-enc ENC] [-dec DEC] [-r R] [-e E] [-n N] [-d D]

Call function from pubcrypt module

options:
  -h, --help  show this help message and exit
  -g G        Generate an RSA keypair. Indicate the bits size as an argument
  -enc ENC    encryption your data
  -dec DEC    decrypt your data
  -r R        recover your primes factor. Indicate the public modulus as an argument
  -e E        Public exponent. By default: e=65537
  -n N        Public modulus
  -d D        Private exponent
``` 

Examples:
```bash
python3 app.py -g 2048
python3 -enc 12 -e 65537 -n 187
```

# Roadmap

Actual todo-list:

- OAEP scheme for encryption and decryption
- PSS scheme for signature
- A document with benchmark result that is automatically generated
- Create the CONTRIBUTING.md and CODE_OF_CONDUCT.md files
- Make a test file
- More cryptosystem ?

# Features 
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