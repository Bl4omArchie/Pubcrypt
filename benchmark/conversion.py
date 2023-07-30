import time, random

min = pow(2, 1023)
max = pow(2, 1024)

def get_time_converting(n):
    result_old = []
    result_new = []

    for _ in range(n):
        start_time = time.time()
        int_to_bin(random.randint(min, max))
        result_old.append(time.time() - start_time)

    for _ in range(n):
        start_time = time.time()
        int_to_bin_new(min, max)
        result_new.append(time.time() - start_time)
    return result_old, result_new


def int_to_bin(n, iter="big"):
    result = ""
    while n > 0:
        if n%2 == 0:
            result += "0"
        else:
            result += "1"
        n = n //2
        
    if iter == "little":
        return result
    else:
        return result[::-1]
    
def int_to_bin_new(n, iter="big"):
    result = ""
    
    while n > 0:
        bit = n & 1  # Obtient le bit le plus à droite de n
        result += str(bit)
        n = n >> 1   # Décalage de n vers la droite d'une position (équivalent à n // 2)

    if iter == "little":
        return result[::-1]
    else:
        return result[::-1]