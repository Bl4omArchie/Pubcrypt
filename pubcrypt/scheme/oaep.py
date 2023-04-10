from pubcrypt.number.random import RBG, bytes_to_int, int_to_bytes, MGF
from pubcrypt.cryptosystem.rsa import primitive_exp
from hashlib import sha384

HASH_INPUT_LIMITATION = pow(2, 61)


def rsa_oaep_encrypt(m, e, n, label):
    message_len = len(m)
    label_len = len(label)
    k = len(n)

    if label > HASH_INPUT_LIMITATION: raise ValueError ("label too long")

    if message_len > k-2*label_len-2: raise ValueError("message too long")
    
    if label == None:
        lHash = "0x8b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b"
    else:
        lHash = sha384(label)
    hash_len = len(lHash)

    ps = RBG(k-message_len-2*hash_len-"0x00")
    db = hash_len | ps | "0x01" | m
    
    seed = RBG(hash_len)
    dbMask = MGF(seed, k-hash_len-1)
    maskedDB = db ^ dbMask
    seedMask = MGF(maskedDB, hash_len)
    maskedSeed = seed ^ seedMask
    em = "0x00" | maskedSeed | maskedDB

    em = bytes_to_int(em)
    ciphertext = primitive_exp(m, e, n)
    return int_to_bytes(ciphertext)