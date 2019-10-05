# -*- coding: utf-8 -*-

'''
    辗转相除法
'''


def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m % n)


# r = gcd(5, 5)
#
# print('r is', r)


p1 = (1, 11)
p2 = (5, 3)


v_v = abs(p1[1] - p2[1])

h_v = abs(p1[0] - p2[0])

r = gcd(v_v, h_v)

print('r is', r)
# v_step = v_v // r
# h_step = h_v // r

v_step = (p2[1] - p1[1]) // r
h_step = (p2[0] - p1[0]) // r

k = r - 1

res = []

for i in range(1, k + 1):
    # print('i is', i)
    p = (p1[0] + h_step * i, p1[1] + v_step * i)
    # print(p)
    res.append(p)

print('res is', res)




