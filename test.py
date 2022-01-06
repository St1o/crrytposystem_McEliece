import numpy as np
# -*- coding: utf-8 -*-


from data_wiki import *

lst = '01100001011000010111001101100110'


def encode(a):
    return list(map(lambda x: "{0:b}".format(ord(x)).zfill(8), a))


def text_from_bits(lst, encoding='utf-8', errors='surrogatepass'):
    n = int(lst, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


print(text_from_bits(lst))
