from pubcrypt.number.util import int_to_string, string_to_int
from pubcrypt.cryptosystem.rsa import primitive_exp
from pubcrypt.number.random import RBG
from hashlib import sha1


HASH_INPUT_LIMITATION = sha1().digest_size



def rsa_oaep_encrypt(message, e, n, label=b''):
    k = n.bit_length()
    mLen = len(message)
    
    if mLen > k - 2 * HASH_INPUT_LIMITATION - 2: raise ValueError("message too long")
    
    if len(label) > HASH_INPUT_LIMITATION - 1: 
        raise ValueError("label too long")
    else:
        label = b'da39a3ee5e6b4b0d3255bfef95601890afd80709'


    lHash = sha1(label).digest()
    PS = b'\x00' * (k - mLen - 2 * HASH_INPUT_LIMITATION - 2)
    DB = lHash + PS + b'\x01' + message


    seed = RBG(HASH_INPUT_LIMITATION)
    dbMask = MGF(seed, k - HASH_INPUT_LIMITATION - 1)


    maskedDB = bytes([DB[i] ^ dbMask[i] for i in range(len(dbMask))])
    seedMask = MGF(maskedDB, HASH_INPUT_LIMITATION)
    maskedSeed = bytes([seed[i] ^ seedMask[i] for i in range(len(seedMask))])


    EM = b'\x00' + maskedSeed + maskedDB
    c = primitive_exp(int.from_bytes(EM, byteorder='big'), e, n)
    return string_to_int(c, order='big')


def MGF(seed, maskLen):
    # MGF1 (Mask Generation Function 1) based on SHA-1
    T = b''

    for i in range((maskLen + HASH_INPUT_LIMITATION - 1) // HASH_INPUT_LIMITATION):
        C = i.to_bytes(4, byteorder='big')
        T += sha1(seed + C).digest()
    return T[:maskLen]