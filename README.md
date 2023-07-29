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
    - [✅ Main branch](#-main-branch)
    - [🚧 pubcrypt-dev](#-pubcrypt-dev)
  - [Version](#version)
  - [Author](#author)
  - [References](#references)

##  Installation

Install the very last version: ```git clone https://github.com/Bl4omArchie/pubcrypt``` <br>
Install the last stable version: https://github.com/Bl4omArchie/pubcrypt/releases/tag/v1.2

Once you installed the package, you can call function from the test.py file.
With the app.py file, call directly your function from the command line:
``` 
usage: app.py [-h] [-g G] [-b B] [-enc ENC] [-dec DEC] [-r R] [-e E] [-n N] [-d D]

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
p, q = first and second prime factor <br>
``` 

------------------------------------------

pubcrypt/number/primality.py:
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| get_prime_factors      | pBits, e        |  a prime p         |
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

My benchmark is comparing different implementation of a same algorithm by mesuring the time it take for N executions.
At the end it generate graph with matplotlib so you visualize the result. It save the picture in this folder: **benchmark/graph**.

In the same folder, I've made a script for every function I want to evaluate. For example, in the gcd.py script, I putted different implementation of the gcd() function and at the end, I can see which one is the more efficient and put in my library.

You can regenerate every graph with the **-b** option in the command line version or calling the **launching_bench()** function in test.py
Example: 
```
python3 app.py -g 2048
``` 
It will repeat every function 10 times.

## Features

### ✅ Main branch
- RSA keypair generation function: generate()
- Factor recovery from public and private key: prime_recovery()
- Random Prime Generator: get_prime_factor() and miller_rabin()
- Command line version: app.py
- Improvement of Miller-Rabin (see pdf in the pdf folder)

### 🚧 pubcrypt-dev
- improve app.py with a file argument where you can indicate your value directly from a file.
- OAEP: encryption, decryption and signature methods
- file format PEM


## Version

| Version          | Description     |
| :--------------: |:---------------:|
| v1.0             | first stable version of pubcrypt. Can generate, encrypt, decrypt and recover prime factors        |
| v1.1             | command line version added        |
| v1.2             | miller-rabin improvement that allow to generate key pairs faster      |


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