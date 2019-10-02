# -*- coding: utf-8 -*-

'''

    去掉字符串中连续出现的k个0

    eg:
        a0000b, k = 3
    output:
        a0b
'''

import re


k = 3

# s = 'a000b0000c000d'
s = '000abd000'


index = 0
res = []
while index < len(s):

    if s[index] == '0':
        kk = k
        index2 = index + 1
        while index2 < len(s) and s[index2] == '0':

            index2 += 1

        span = index2 - index

        if span >= k:

            res.append(s[index + k: index2])

            index = index2
        else:
            res.append(s[index: index2])
            index = index2
            # index += span

    else:
        res.append(s[index])
        index += 1


r = ''.join(res)
print('res is', r)
