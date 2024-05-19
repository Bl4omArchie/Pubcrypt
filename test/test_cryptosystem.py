from pubcrypt.cryptosystem import rsa

"""
This script perform test on the RSA cryptosystem function and primitives implemented in Pubcrypt
"""

def test_key_generation():
    """ Test #01: verify the generate() function for various key size."""
    key_size = [2048, 3072, 4096]

    print ("--------------------------------------")

    try:
        for key in key_size:
            rsa.generate(key)
            print (f"> Test valid for key size: {key}")
    except:
        print (f"[!] Test #01 has failed for key size {key}")
        print ("--------------------------------------")
        return -1
    print ("[+] Test complete: 100% sucessful")
    
    print ("--------------------------------------")