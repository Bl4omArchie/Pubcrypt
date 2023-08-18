# Pubcrypt ~ RSA keypair

This library aim to generate an RSA keypair in python. 
Other features like encryption, decryption and prime_factor recovery are available. 
I've started this project in the purpose of training myself to implemente cryptographic algorithm. In consequence, this library do NOT aim for a profesional purpose.


## Table of contents
- [Pubcrypt ~ RSA keypair](#pubcrypt--rsa-keypair)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Documentation](#documentation)
  - [Benchmark](#benchmark)
  - [Features](#features)
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

```
nBits = the size in bits of your key [2048, 8192] <br>
n = public modulus <br>
e = public exponent <br>
d = private exponent <br>
exp = public or private exponent <br>
p, q = first and second primeArithmetic algorithm: gcd, lcm, sqrt, fast_exponentiation, 
 factor <br>
``` 

------------------------------------------

pubcrypt/number/primality.py:
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| get_prime_factors      | pBits, e        |  prime factor p and q         |
| miller_rabin           | p, r            | PRIME or NOT_PRIME |

``` 
r = number of round for Miller Rabin primality test. Set to 5
``` 

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
| RNG                    | nBits           | an integer of nBits            |

-----------------------------------------------------


A more precise description is available below each function


## Benchmark

After few differents attempts, I finally find out the best way to evaluate my code effiency and write a decent benchmark so that my coding environnement could be perfect.
I recently eard about cProfile, a default packages of the python language that offer a very code tracability of the code behaviour. 
For instance, if you want to test a function, this package will create a profile that show the execution time of the function but also ...

With this package, I can write a clean benchmark: every function has is profile, I can precisly see if the function is efficient and if not, what part of the function is slow. Then, I can easily extract this data, so I could plot them in a graph with matplotlib. 
I can easily add a function to the benchmark or remove it.

## Features

Main product:
- RSA keypair generator
- RSA message encryption and decryption
- RSA prime factors recovery


## Version

| Version          | Description     |
| :--------------: |:---------------:|
| v1.0             | first stable version of pubcrypt. Can generate, encrypt, decrypt and recover prime factors        |
| v1.1             | command line version added        |
| v1.2             | miller-rabin improvement that allow to generate key pairs faster      |
| v1.3             | correction of the get_prime_factor function |


## Author
You can contact me and see my work here:
- Blog: https://bl4omarchie.github.io/archX/
- Discord server: https://discord.com/invite/D2wGP62
- Twitter: https://twitter.com/Bl4om_Archie

## References
 - [NIST FIPS 186-4: Digital Signature Standard (DSS)](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.186-4.pdf)
 - [NIST SP 800-56Br2: Recommendation for Pair-Wise Key Establishment Using Integer Factorization Cryptography](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br2.pdf)
 - [PKCS #1 Version 2.2: RSA Cryptography Specifications draft-moriarty-pkcs1-01](https://datatracker.ietf.org/doc/pdf/draft-moriarty-pkcs1-01.pdf)
 - [RosettaCode](https://rosettacode.org/wiki/Rosetta_Code)