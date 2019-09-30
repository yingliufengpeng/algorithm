# -*- coding: utf-8 -*-

''''
    在非负数组(乱序)中找到最小的可分配的id(从1开始编号),数量1 * (10 ** 3)

    这种方法是借助了临时数组的模式来做这样的操作

    使用这种模式的数组可以获得最小计数的问题
'''

nums = list(range(10, -1, -1))
nums.pop(2)
# nums.pop(2)

print('nums is', nums)

nums_new = [0] * len(nums)

print('nums_new is', nums_new)

for e in nums:
    if e >= len(nums_new):
        continue
    nums_new[e] = 1

print(nums_new)

res = False
index = 0
for i, e in enumerate(nums_new):

    if e == 0:
        index = i
        res = True
        break

if res:

    print('res is ', res)
    print('index is ', index)

else:
    print('index is', len(nums_new))
