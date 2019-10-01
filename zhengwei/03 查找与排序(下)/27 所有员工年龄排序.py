# -*- coding: utf-8 -*-

'''
    公司现在要对几万员工的年龄进行排序,因为公司员工的人数非常多,所以要求的排序
    算法的效率非常高,你能写出这样的程序吗?

    该方法是计数排序的方法
'''

import random

# 公司员工的年龄是一个很大的列表
nums = [random.randint(1, 99) for _ in range(10 ** 2)]

print('所有的员工的年龄为: ', nums)

count_nums = [0] * 100      # 使用计数排序的思路, 0-99 个坑位

for age in nums:

    count_nums[age] += 1

print('常规排序为: ', sorted(nums[:]))

print('count_nums is', count_nums)

index = 0

for age, count in enumerate(count_nums):
    if age == 0:   # 跳去第0个元素的值,因为我们不需要这个值
        continue

    for i in range(count):
        # print('index is', index)
        nums[index] = age
        index += 1

print('排序后的年龄为: ', nums)





