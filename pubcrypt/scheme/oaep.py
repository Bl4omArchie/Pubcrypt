from random import getrandbits
import hashlib

Hash = hashlib.new("sha256")
hlen = Hash.digest_size

def rsa_oaep_encrypt(plaintext, n, e, label=b''):
    mLen = len(plaintext)
    k = len(n.to_bytes((n.bit_length() + 7) // 8, byteorder='big'))

    if len(label) > hlen:
        raise ValueError("label too long")
    
    if mLen > k - 2*hlen - 2:
        raise ValueError("Message too long")

    if label == b'':
        label = b"0xe3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    PS = b'\x00' * (k - mLen - 2 * hlen - 2)
    DB = bytes(hlen) | PS | b'\0x01' | plaintext
    
    seed = getrandbits(hlen)
    db_mask = MGF(seed, k-hlen-1)
    maskedDB = bytes(a ^ b for a, b in zip(DB, db_mask))
    seedMask = MGF(maskedDB, hlen)
    maskedSeed = bytes(a ^ b for a, b in zip(seed, seedMask))

    return b'\0x00' | maskedSeed | maskedDB


def MGF(seed, mask_len):
    mask = b""
    iterations = (mask_len + hlen - 1) // hlen

    for counter in range(iterations):
        counter_bytes = counter.to_bytes(4, byteorder='big')
        data = seed + counter_bytes
        mask += hashlib.new("sha256", data).digest()

    return mask[:mask_len]
