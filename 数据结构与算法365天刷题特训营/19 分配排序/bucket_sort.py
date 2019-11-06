# -*- coding: utf-8 -*-

# 对0-100中的数据进行桶排序, 桶的个数为10
# 桶的取值区间为 [i, i + 10), i = 0, 10, 20  i < 100
import random
N = 10

buektes = [[] for _ in range(N)]    # 注意 使用 [[]] * N 这种模式会导致[]是个公共的变量指向同一份指针

M = 100

for _ in range(M):

    e = random.randint(0, 99)

    index = e // N

    buektes[index].append(e)

res = []

for vs in buektes:

    res.extend(sorted(vs))

print('res is', res)

print('res == sorted(res)', res == sorted(res))
