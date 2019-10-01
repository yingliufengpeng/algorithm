# -*- coding: utf-8 -*-

'''
    输入一个正整数数组,把数组里所有的整数拼接起来排成一个数,打印出拼接出的所有
    数字中最小的一个

    例如:
        [3, 32, 321] 最小数为: 321323
'''


import functools

nums = [3, 321, 32]

print('before nums', nums)


'''
    比较器的规则, 当 x < y的时候, 我们就返回 -1, 否则我们就返回+1
'''


def cmp(x, y):
    x = str(x)
    y = str(y)
    if x < y:
        return -1
    else:
        return +1


b = sorted(nums, key=functools.cmp_to_key(cmp), reverse=True)

print('b is', b)

res = ''.join(str(i) for i in b)
print('after nums', int(res))
