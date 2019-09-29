# -*- coding: utf-8 -*-

a = 16


b = bin(a)

c = b.count('1')

if c in [0, 1]:
    print(True)
else:
    print(False)