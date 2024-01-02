from pubcrypt.number.util import string_to_int, int_to_string
from random import getrandbits
import hashlib, math

"""
Signature scheme: PSS
"""

Hash = hashlib.new("sha256")
hLen = Hash.digest_size     #input limitation of sha256
sLen = 16                   #16 bits salt

def pss_encode(m, emBits, hash_function=hashlib.sha256):
    if len(m) > hLen:
        raise ValueError("Message too long")
    
    mHash = hash_function(m).digest()

    if emBits < hLen + sLen+2:
        raise ValueError("Encoding error")

    salt = bytes(getrandbits(sLen))
    mP = b'\x00\x00\x00\x00\x00\x00\x00\x00' + mHash + salt
    H = hash_function(mP).digest()

    ps_len = len(m) - sLen - hLen - 2
    PS = b'\x00' * ps_len

    DB = PS + b'0x01' + salt 
    DB_mask = mgf(H, emBits - hLen - 1)


    masked_db = bytes(a ^ b for a, b in zip(DB, DB_mask))   #xor
    masked_db = bytearray(masked_db)
    masked_db[0] &= math.ceil((2**(8 * len(m) - emBits) - 1))

    return bytes(masked_db) + H + b'\xbc'


def mgf(seed, mask_len, hash_function=hashlib.sha256):
    t = b''
    for counter in range((mask_len + hash_function().digest_size - 1) // hash_function().digest_size):
        c = int.to_bytes(counter, 4, byteorder='big')
        t += hash_function(seed + c).digest()
    return t[:mask_len]


def signature_pritimive(m, d, n):
    # Check if m is in the range [0, n-1]
    n = K[0] if len(K) == 2 else K[0] * K[1]  # n is the product of p and q if the second form is used
    if not (0 <= m < n):
        raise ValueError("message representative out of range")

    # Compute the signature representative s
    if len(K) == 2:                 # First form (n, d)
        _, d = K
        s = pow(m, d, n)

    else:                           # Second form (p, q, dP, dQ, qInv) and (r_i, d_i, t_i)
        p, q, dP, dQ, qInv = K[:5]
        u = (len(K) - 5) // 3
        s1 = pow(m, dP, p)
        s2 = pow(m, dQ, q)

        if u > 2:
            s = s2 + q * ((s1 - s2) * qInv % p)
            R = K[5]
            for i in range(3, len(K), 3):
                s_i = pow(m, K[i + 1], K[i])
                R *= K[i - 1]
                h = (s_i - s) * K[i + 2] % K[i]
                s += R * h
        else:
            h = (s1 - s2) * qInv % p
            s = s2 + q * h

    return s



def signature_generation(m, d, n, nBits):
    em = pss_encode(m, nBits-1)
    m = string_to_int(em)
    s = signature_pritimive(m, d, n)
    return int_to_string(s)