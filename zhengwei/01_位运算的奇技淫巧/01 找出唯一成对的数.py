# -*- coding: utf-8 -*-

N = 10
a = list(range(1, N + 1))
a.append(9)

r = 0

# 首先,先把前N个数值异或一遍,因为只有一个元素相同,所以已经把所有的数值都异或到,而不用考虑最后一个数值
for e in a[0:-1]:
    r ^= e

# 然后在异或所有的数值,因为是所有的数据,所以有两个相同的值,所以最终额结果则是那个相同的值的情况
for e in a:
    r ^= e

print('a is {}'.format(a))

print('r is ', r)



