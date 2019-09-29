# -*- coding: utf-8 -*-


def han(a, b, c, n):
    if n == 0:
        return
    han(a, c, b, n - 1)
    print('{} -> {}'.format(a, c))
    han(b, a, c, n - 1)


han('a', 'b', 'c', 10)
