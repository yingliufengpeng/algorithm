# -*- coding: utf-8 -*-

'''
    两串的字符集是否相同

    eg:
        s1 = 'abbbd', s2 = 'abd'

    out:
        两者的字符集相同
'''

s1 = 'abbbdefg'
s2 = 'abddddfddge'

set1 = set(s1)
set2 = set(s2)

res = set1 & set2 == set1 | set2

print('res is', res)
