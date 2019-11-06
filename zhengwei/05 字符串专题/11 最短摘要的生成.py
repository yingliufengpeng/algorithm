# -*- coding: utf-8 -*-

'''
    kmp,后缀与前缀的最长匹配长度
'''

from decimal import Decimal

# nums = list(range(10))
#
nums = [5]

target = 5

le = 0
ri = len(nums) - 1

while le <= ri:  # 做种终止条件则是le > ri这样的情况!!! le = ri + 1

    mid = (le + ri) // 2
    v = nums[mid]

    if v == target:
        print('got it!!!')
        break

    if target > v:
        le = mid + 1

    else:
        ri = mid - 1
