from hashlib import sha1

class HASH_SHA1():
    INPUT_LIMIT = pow(2, 61)-1
    default_label = 0x5e6b4b0d3255bfef95601890afd80709
    hLen = 160

    def __init__(self) -> None:
        pass

    def hash(self):
        pass

    def mask_function(self, seed, mask_len):
        if mask_len > pow(2, 32): raise ValueError("Mask too long")