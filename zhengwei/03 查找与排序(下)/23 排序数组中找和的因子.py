# -*- coding: utf-8 -*-

'''
    给定已排序的数组nums和k,不重复打印nums中所有相加和为k的不降序的二元组

    eg:
        nums = [-8, -4, -3, 0, 2, 4, 5, 8, 9, 10], k = 10

    out:
        (0, 10), (2, 8)
'''

nums = [-8, -4, -3, 0, 2, 4, 5, 8, 9, 10]

be = 0
end = len(nums) - 1

k = 2

res = []

while be < end:

    if nums[be] + nums[end] == k:
        res.append((nums[be], nums[end]))
        be += 1
    elif nums[be] + nums[end] < k:
        be += 1
    else:
        end -= 1

print('res is ', res)
