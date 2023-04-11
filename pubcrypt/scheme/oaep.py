from pubcrypt.number.random import RBG, int_to_string, string_to_int
from pubcrypt.cryptosystem.rsa import primitive_exp
from pubcrypt.hash.sha1 import HASH_SHA1
from hashlib import sha384

HASH_INPUT_LIMITATION = pow(2, 61)


def rsa_oaep_encrypt(m, e, n, label):
    message_len = len(m)
    label_len = len(label)
    k = len(n)

    if label > HASH_INPUT_LIMITATION: raise ValueError ("label too long")

    if message_len > k-2*label_len-2: raise ValueError("message too long")
    
    hash_obj = HASH_SHA1()

    ps = RBG(k-message_len-2*hash_obj.hLen-"0x00")
    db = hash_obj.hLen | ps | "0x01" | m
    
    seed = RBG(hash_obj.hLen)
    dbMask = hash_obj.mask_function(seed, k-hash_obj.hLen-1)
    maskedDB = db ^ dbMask
    seedMask = hash_obj.mask_function(maskedDB, hash_obj.hLen)
    maskedSeed = seed ^ seedMask
    em = "0x00" | maskedSeed | maskedDB

    em = string_to_int(em)
    ciphertext = primitive_exp(m, e, n)
    return int_to_string(ciphertext)