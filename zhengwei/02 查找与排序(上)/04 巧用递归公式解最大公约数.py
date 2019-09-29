# -*- coding: utf-8 -*-


def gcd(m, n) -> int:
    if n == 0:
        return m

    return gcd(n, m % n)


r = gcd(2, 3)

print('r is', r)
