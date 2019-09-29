# -*- coding: utf-8 -*-

# 出现k次
# 数组中其他出现K次,而只有一个值只出现一次

# 所需的解法,通过进制的逻辑来实现


k = 3

a = []

for i in range(10):
    a.extend([i] * k)

a.append(6)


# 进制转换
def f(n, x):
    # n为待转换的十进制数，x为进制，取值为2-16
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
    b = []
    while True:
        s = n // x  # 商
        y = n % x  # 余数
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    # print('做相关的进制转换的逻辑')
    # for i in b:
    #     print(a[i], end='')

    return b


print('十进制', a)

b = [f(n, k) for n in a]

print('k进制', b)

# 对k进制数进行各个位进行不进位加一

# 获得每个子列表的最大的长度
maxl = max(len(li) for li in b)

# maxl = k

print('maxl is', maxl)

r = []

for li in b:
    c = [0] * maxl

    c[maxl - len(li):] = li[:]

    r.append(c)

print('r is', r)

res = [0] * maxl

for l2 in r:

    r3 = []

    r2 = zip(l2, res)

    for (e1, e2) in r2:
        v = (e1 + e2) % k
        r3.append(v)

    res = r3

print('res', res)

s = 0
for i, e in enumerate(res):
    s += e * (k ** (maxl - 1 - i))

print('s is', s)
