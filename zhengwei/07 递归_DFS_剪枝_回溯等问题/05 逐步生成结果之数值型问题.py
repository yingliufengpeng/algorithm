# -*- coding: utf-8 -*-

'''
    此时这类问题就需要用容器去装了
'''

'''
    实现一种算法,打印n对括号的全部有效的组合(即左右括号正确配对)
'''


# 递归模式的方案
def slove(n):
    if n == 1:
        return {'()'}

    set_n = set()

    res = slove(n - 1)

    for e in res:
        set_n |= {
            '(){}'.format(e),
            '({})'.format(e),
            '{}()'.format(e),
        }

    return set_n


# r = slove(10)
# print('r is', r)
# print('len of r is', len(r))


# 通过迭代的模式来实现此功能

def solve2(n):
    res = {'()'}

    if n == 1:
        return res

    for i in range(2, n + 1):
        new_set = set()

        for e in res:
            new_set |= {
                '(){}'.format(e),
                '({})'.format(e),
                '{}()'.format(e),
            }

        res = new_set

    return res


r = solve2(16)

print('r is', r)
print('len of r is', len(r))
