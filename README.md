# Pubcrypt ~ RSA keypair

This library aim to generate an RSA keypair in python. 
Other features like encryption, decryption and prime_factor recovery are available. 
I've started this project in the purpose of training myself to implemente cryptographic algorithm. In consequence, this library do NOT aim for a profesional purpose.


## Table of contents
- [Pubcrypt ~ RSA keypair](#pubcrypt--rsa-keypair)
  - [Table of contents](#table-of-contents)
  - [Installation](#installation)
  - [Documentation](#documentation)
  - [Task](#task)
    - [🚧 In progress](#-in-progress)
    - [✅ Done](#-done)
  - [Version](#version)
  - [Author](#author)
  - [References](#references)

##  Installation

Install the very last version: ```git clone https://github.com/Bl4omArchie/pubcrypt```
Install the last stable version: https://github.com/Bl4omArchie/pubcrypt/releases/tag/v1.0

Once you installed the package, you can call function from the test.py file

## Documentation

pubcrypt/cryptosystem/rsa.py
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| generate               | nBits, e=65537  |  public and private keypair: n, e, d   |
| primitive_exp          | m, exp, n       |   plaintext or ciphertext  |
| prime_recovery         | n, e, d         |    p, q |

nBits = the size in bits of your key [2048, 8192]
n = public modulus
e = public exponent
d = private exponent
exp = public or private exponent
p, q = first and second prime factor 

------------------------------------------

pubcrypt/number/primality.py:
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| get_prime_factors      | pBits, e        |  a prime p         |
| miller_rabin           | p, r            | PRIME or NOT_PRIME |
r = number of round for Miller Rabin primality test. Set to 5

-----------------------------------

pubcrypt/number/random.py:
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| get_prime_factors      | pBits, e        |  a prime p         |
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
| perfect_square         | c               | PERFECT_SQUARE or NOT_PERFECT_SQUARE |

-----------------------------------------------------

pubcrypt/number/random.py
| functions              | Parameters      | Return             |
| :--------------:       |:---------------:| :-----------------:|
| RBG                    | nBits           | a bit string of nBits          |
| RNG                    | nBits           | an integer of nBits            |
| int_to_bytes           | a, b            | a bit string representing the integer x    |
| bytes_to_int           | m, e, n         | an integer representing the string x       |


A more precise description is available below each function


## Task

### 🚧 In progress
- benchmark + pdf with graph an tutorial
- app.py: where you can use the library with command from the terminal
- PKCS: encryption, decryption and signature methods

### ✅ Done
- generate(), primitive_exp(), prime_factor_recovery()
- Miller Rabin primality test
- README + gitignore


## Version

| Version          | Description     |
| :--------------: |:---------------:|
| v1.0             | first stable version of pubcrypt. Can generate, encrypt, decrypt and recover prime factors        |


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