# -*- coding: utf-8 -*-

'''
    计数排序: 需要额外开辟空间,所以在原始数组中的最大值不能太大,一般不超过1000即可
'''


nums = [1, 20, 3, 40, 2, 34, 59, 13, 26, 3, 3]

N = 1000
help_nums = [0] * (N + 1)

for e in nums:
    help_nums[e] += 1

res = []


for i, e in enumerate(help_nums[1:]):

    v = e

    res.extend([i + 1] * v)

    # while v > 0:
    #     res.append(i + 1)
    #     v -= 1

print('res is ', res)

