import time


b = 365464156156456
c = 56464654684646

b_bin = 0b1010011000110001101000001001101001011001000101000
c_bin = 0b1100110101101010110011101011110101000111100110




start_time = time.time()
a = b >> 2
print (time.time() - start_time)

start_time = time.time()
a = b_bin >> 2
print (time.time() - start_time)