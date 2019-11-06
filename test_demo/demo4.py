# -*- coding: utf-8 -*-

i = 123
res = []
while 123 <= i <= 333:

    v = set()

    aa, bb, cc = i, i * 2, i * 3

    a, b, c = [int(e) for e in str(aa)]
    a2, b2, c2 = [int(e) for e in str(bb)]
    a3, b3, c3 = [int(e) for e in str(cc)]

    v |= {a, b, c, a2, b2, c2, a3, b3, c3} - {0}

    if len(v) == 9:

        res.append('{} {} {}'.format(aa, bb, cc))

    i += 1

for vs in res:
    print(vs)

'''
    192 384 576
    219 438 657
    267 534 801
    273 546 819
    327 654 981
'''