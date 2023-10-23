from pubcrypt.parallel.rsa_engine import clock
import time

if __name__ == "__main__":
    current_time = time.gmtime()
    print(current_time.tm_hour)