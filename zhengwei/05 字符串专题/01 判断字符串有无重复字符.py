# -*- coding: utf-8 -*-

'''
    判断字符串是否有无重复字符串
'''

from collections import defaultdict

d = defaultdict(int)

s = 'abcdefg'


def issamechar(s):
    for e in s:

        if d[e] > 0:
            return True
        else:

            d[e] += 1

    return False


r = issamechar(s)

print('是否有重复的字符串: ', r)
