from pubcrypt.number.util import int_to_string, string_to_int
from pubcrypt.cryptosystem.rsa import primitive_exp
from pubcrypt.number.util import RBG
from hashlib import sha1

labels = {
    "sha1": b"0xda39a3ee5e6b4b0d3255bfef95601890afd80709",
    "sha256": b"0xe3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "sha384": b"0x38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b",
    "sha512": b"0xcf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e"
}

HASH_INPUT_LIMITATION = sha1().digest_size


def rsa_oaep_encrypt(message, e, n, hash="sha1", label=b''):
    k = n.bit_length()
    mLen = len(message)
    
    if mLen > k - 2 * HASH_INPUT_LIMITATION - 2: raise ValueError("message too long")
    
    if len(label) > HASH_INPUT_LIMITATION - 1: 
        raise ValueError("label too long")
    else:
        label = labels[hash]


    lHash = sha1(label).digest()
    PS = b'\x00' * (k - mLen - 2 * HASH_INPUT_LIMITATION - 2)
    DB = lHash + PS + b'\x01' + message


    seed = RBG(HASH_INPUT_LIMITATION)
    dbMask = MGF(seed, k - HASH_INPUT_LIMITATION - 1)


    maskedDB = bytes([DB[i] ^ dbMask[i] for i in range(len(dbMask))])
    seedMask = MGF(maskedDB, HASH_INPUT_LIMITATION)
    print (seed)
    print (seedMask)
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