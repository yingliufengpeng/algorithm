# -*- coding: utf-8 -*-

# def pow0(a: int, n: int) -> int:
#     if n == 0:
#         return 1
#
#     return a * pow0(a, n - 1)

#
# r = pow0(2, 3)
# print('r is ', r)

'''
    高效的模式的确很高效的策略
'''


def pow2(a: int, n: int) -> int:
    if n == 0:
        return 1

    res = a
    ex = 1

    while ex << 1 <= n:
        res *= res
        ex <<= 1

    return res * pow2(a, n - ex)


r2 = pow2(10, 3)

print('r2 is ', r2)
