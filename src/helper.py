"""Small helper"""
from math import log

def hex2bin(hexstr):
    scale = 16
    num_of_bits = len(hexstr)*log(scale, 2)
    binstr = bin(int(hexstr, scale))[2:].zfill(int(num_of_bits))
    return binstr

def bin2int(binstr):
    return int(binstr, 2)

def bin2hex(binstr):
    return "%X" % int(binstr, 2)
