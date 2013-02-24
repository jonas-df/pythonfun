#!usr/bin/ python

import sys

number = sys.stdin.read()
binary_number = bin(int(number))
bits = [bit for bit in binary_number][2:]
bits.reverse()
rev_number = '0b'+''.join(bits)
print int(rev_number,2)

