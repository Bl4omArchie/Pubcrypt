# %% [markdown]
#  # Rapport projet Pubcrypt: gestion et génération d'une paire de clé RSA
# 
#  Abstract: Ce rapport vise à résumer le travail que j'ai effectué sur le projet Pubcrypt. Il retrace chaque étapes, explique mes choix et pour chaque algorithme je propose un benchmark ainsi qu'une amélioriation de l'algorithme.
#  J'espère que cela peut aider d'autre personne à comprendre le chiffrement RSA et servir de tutoriel pour implémenter un tel cryptosystème.
# 
# 
#  # Sommaire
#   Table of contents:
# 
# 
# 
#  # Les objectifs de Pubcrypt
# 
# Lorsque j'ai commencé ce projet, je me suis fixé les objectifs suivants:
# - mettre en pratique mes connaissances sur le chiffrement RSA
# - apprendre les normes spécifiques pour produire une implémentation correcte
# - améliorer la performance de mes algorithmes pour produire un programme efficace
# 
# J'aime la cryptographie, mais j'aime avant tout la programmation. Ce qui m'intéresse le plus c'est d'apprendre à implémenter les algorithmes et les techniques de développement pour les accélérer. Dans ce projet, je mets donc surtout en avant l'efficacité du code.
# 
#  # RSA: un cryptosystème délicat à implémenter
# 
#  Avant de commencer ce projet, je faisais des challenges sur la plateforme cryptohack[1] qui permet d'apprendre ou de mettre en application ses connaissances en cryptographie. Ces challenges énumèrent de nombreuses situations où RSA est compromis à cause de conditions non respectées.
#  En effet, RSA est délicat à implémenter car depuis sa création, de nombreuses attaques de cryptanalyse ont montré que s'écarter des normes est très une mauvaise idée car la sécurité que procure une paire de clé RSA est alors brisée.
# 
#  Il faut donc s'armer correctement avec les normes nécessaires pour éviter les erreurs. Pour cela je vous propose ces deux documents provenant du NIST très pratiques: FIPS 186-4[2] et sp800-56[3]. Le NIST est un institut américain de normalisation qui a normalisé de nombreux algorithmes comme RSA, AES et autre.
#  Pour Pubcrypt je m'en suis inspiré comme base car la documentation est plutôt explicite et complète.
#  Voyons à quoi ressemble ces normes.
# 
#  ## Les normes RSA selon la publication sp800-56 du NIST
# 
#  Sur les deux documents que je vous ai fournis ci-dessus, c'est avec le sp800-56 dont nous auront besoin en premier. Ce document nous explique comment gérer notre paire de clé et comment la générer dans la section 6: RSA keys pairs. Dans la section 6, nous avons besoin des sous-parties 6.2 et 6.3, les autres sous-parties sont des normes qui s'aplliquent à une gestion plus large de notre paire de clé (ex: certificat, droit d'accès etc).
# 
# 
# 

# %% [markdown]
#  # Création des algorithmes arithmétiques
# 
#  Dans cette partie nous implémentons les algo arithmétiques nécessaires. En voici la liste:
#  - pgcd
#  - racine carré (sqrt)
#  - exponentiation modulaire (pow_fast)
#  - inverse modulaire (invmod)
#  - conversion d'entiers en chaîne de caractère
#  - conversion de chaîne de caractère en entiers
#  - conversion d'entier en nombre binaire
# 
# 
# 
#  ## PGCD
# 
#  En premier lieu, j'ai développé cet algorithme. Il est simple, tiens en quelques lignes, c'est la solution que l'on retrouve le plus souvente sur internet:
#  ```py
#  def GCD(x,y):
#      x = abs(x) ; y = abs(y)
#      while x > 0:
#          x, y = y % x, x
#      return y
#  ```
# 
# Sauf que cet algorithme n'est pas performant, j'ai cherché plus loin et j'ai découvert un autre algorithme: le pgcd binaire. Au lieu d'effectuer les opérations sur des nombres entiers (base10), on joue avec les nombres binaires (base2). Vu que nous utilisons seulement le nombre 0 et 1, l'algorithme est donc plus rapide. Ce qui a donné ceci:
# 
#  ```py
#  def gcd(x, y):
#      if x == 0:
#          return y
#      if y == 0:
#          return x
# 
#      x_rightmost = x & -x
#      y_rightmost = y & -y
# 
#      while x_rightmost != y_rightmost:
#          if x_rightmost > y_rightmost:
#              x_rightmost >>= 1
#          else:
#              y_rightmost >>= 1
# 
#      return x_rightmost
#  ```
# 
# Ici je n'utilise plus que des shifts et le ET logique (&).
# Je compare alors ma fonction avec la fonction proposée par python dans le module math:

# %%
from benchmark.plotting import *
from pubcrypt.number.util import *
import math, random

n = 5000
obj = GraphVisualization("GCD comparison")
obj.measure_execution_time(n, gcd, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
obj.measure_execution_time(n, math.gcd, random.randint(2**2048, 2**2049), random.randint(2**2048, 2**2049))
obj.plot_data(["green", "red"], ["gcd()", "python gcd()"], show_stats=True)


# %% [markdown]
#  # References
# 
#  [1] [Digital Signature Standard (DSS) - FIPS 186-4](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.186-4.pdf) <br/>
#  [2] [Recommendation for Pair-Wise Key Establishment Using Integer Factorization Cryptography](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Br2.pdf)<br/>
#  [3] [PKCS #1 Version 2.2: RSA Cryptography Specifications draft-moriarty-pkcs1-01](https://datatracker.ietf.org/doc/pdf/draft-moriarty-pkcs1-01.pdf)<br/>
#  [4] [Finding Large Primes for Public Key Cryptography - Glenn Henshaw](https://ghenshaw-work.medium.com/finding-large-primes-for-public-key-cryptography-9c5a5c0d32c4)<br/>
#  [5] [Mathematics of Public Key Cryptography - Steven D Galbraith](https://www.math.auckland.ac.nz/~sgal018/crypto-book/main.pdf)<br/>
#  [6] An Introduction to Mathematical Cryptography - Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman<br/>
#  [7] FAST GENERATION OF RANDOM, STRONG RSA PRIMES - Robert D. Silverman - RSA Laboratories - May 17, 1997<br/>
#  [8] Cryptosystème RSA - Anca Nitulescu - Ecole Normale Supérieure, Paris<br/>
#  [9] [A Warm Welcome to ASN.1 and DER - Let's Encrypt](https://letsencrypt.org/fr/docs/a-warm-welcome-to-asn1-and-der/)<br/>
#  [10] [Algorithms for Modern Hardware - Sergey Slotin](https://en.algorithmica.org/hpc/)<br/>


