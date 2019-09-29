# -*- coding: utf-8 -*-


def f1(n: int) -> int:
    if n <= 1:
        return 1

    return n * f1(n - 1)


r = f1(5)
print('r is', r)
