# Pubcrypt ~ RSA keypair

This library aim to generate an RSA keypair in python. 
Other features like encryption, decryption and prime_factor recovery are available. 
I've started this project in the purpose of training myself to implemente cryptographic algorithm. In consequence, you shall not use it for real life purpose.


Table of contents:
- [Pubcrypt ~ RSA keypair](#pubcrypt--rsa-keypair)
  - [Installation](#installation)
  - [Documentation](#documentation)
  - [Benchmark](#benchmark)
- [Features](#features)
  - [RSA GMP](#rsa-gmp)
- [Version](#version)
- [Author](#author)
- [References](#references)

##  Installation

Install the very last version: ```git clone https://github.com/Bl4omArchie/pubcrypt``` <br>
Install the last stable version: https://github.com/Bl4omArchie/pubcrypt/releases/tag/v1.2

Once you installed the package, you can call function from the test.py file.
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

## Documentation

pubcrypt/cryptosystem/rsa.py
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| generate               | nBits, e=65537  |  public and private keypair: n, e, d   |
| primitive_exp          | m, exp, n       |   plaintext or ciphertext  |
| prime_recovery         | n, e, d         |    p, q |

------------------------------------------

pubcrypt/cryptosystem/rsa_gmp.py
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| generate_gmp               | nBits, e=65537  |  public and private keypair: n, e, d   |

------------------------------------------

pubcrypt/number/primality.py:
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| get_prime_factors_gmp      | pBits, e, state        |  prime factor p and q         |

----------------------------------------

pubcrypt/number/primality.py:
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| get_prime_factors      | pBits, e        |  prime factor p and q         |
| miller_rabin           | p, r            | PRIME or NOT_PRIME |

----------------------------------------

pubcrypt/number/util.py:
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| invmod                 | a, b            | inverse of a modulo b          |
| gcd                    | a, b            | gcd of a and b |
| lcm                    | a, b            | lcm of a and b |
| pair wise consistency test | m, e, n     | True or False  |
| isqrt                  | x               | square root of x |
| perfect_square         | c               | True if perfect square else False |
| RBG                    | nBits           | a bit string of nBits          |

-----------------------------------------------------


A more precise description is available below each function


## Benchmark

This benchmark intend to evaluate the effiency of Pubcrypt's function
With only two simples class: GraphVisualization and EffiencyProfile, I have access to a good overview of the performance.

- GraphVisualization allow me to generate a graph that plot the times of execution for one or severals function.
- EffiencyProfile generate a profile with the library cProfile which is specialised in examining function in details. It give me information about witch modules are called in the function, how many I have been calling them and the final generation time.
This evaluation is more accurated for huge function that used many external packages.

Find two samples in the benchmark.py file.

# Features
- RSA keypair generator
- RSA message encryption and decryption
- RSA prime factors recovery

- RSA_GMP keypair generator
- RSA_GMP get_prime_factor
- RSA_GMP miller-rabin

## RSA GMP

As I started implementing RSA cryptosystem in C with the GMP library, I was curious to see how much the python GMP library could be faster than mine.
So I implemented another RSA key pairs generator but with the gmpy2 module that you can find in both file: rsa_GMP.py and primality_GMP.py
A graph for the generation of 100 keys with this algorithm is available in the benchmark/graph folder named "RSA GMP generate function".**
The outcome is surrounding: my implementation is, from far, slower ! The python GMP implementation burst everything with a maximal generating time of 2.5 seconds. Still we can notice that the average time is 2.3 seconds while Pubcrypt is 2.4 seconds. 
As a conclusion GMP is more stable than my implementation but not "faster" because the minimal generating time is around 2.2 seconds while pubcrypt go down under the second (0.24s).  

# Version

| Version          | Description     |
| :--------------: |:---------------:|
| v1.0             | first stable version of pubcrypt. Can generate, encrypt, decrypt and recover prime factors        |
| v1.1             | command line version added        |
| v1.2             | miller-rabin improvement that allow to generate key pairs faster      |
| v1.3             | correction of the get_prime_factor function |
| v1.4             | proper versionn with good performance + benchmark |
| v1.5             | new feature: RSA_GMP. Arithemic operations are handled by gmpy2 |

# Author
You can contact me and see my work here:
- Blog: https://bl4omarchie.github.io/archX/
- Discord server: https://discord.com/invite/D2wGP62
- Twitter: https://twitter.com/Bl4om_Archie

# References
 - [NIST FIPS 186-4: Digital Signature Standard (DSS)](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.186-4.pdf)
 - [NIST SP 800-56Br2: Recommendation for Pair-Wise Key Establishment Using Integer Factorization Cryptography](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br2.pdf)
 - [PKCS #1 Version 2.2: RSA Cryptography Specifications draft-moriarty-pkcs1-01](https://datatracker.ietf.org/doc/pdf/draft-moriarty-pkcs1-01.pdf)
 - [RosettaCode](https://rosettacode.org/wiki/Rosetta_Code)
 - [gmpy2 documentation](https://gmpy2.readthedocs.io/en/latest/intro.html)