import binascii

n = int('010001010110111001100111011010010110111001100101011001010111001001101001011011100110011100100000010010000110010101100001011011000111010001101000', 2)
print binascii.unhexlify('%x' % n)
