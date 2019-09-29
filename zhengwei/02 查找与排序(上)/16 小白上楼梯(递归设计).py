# -*- coding: utf-8 -*-

'''
    小白上楼梯,

    使用递归的方法,f(n) = f(n - 1) + f(n - 2)
'''


def fn(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return n

    return fn(n - 1) + fn(n - 2)


r = fn(4)

print('r is', r)
