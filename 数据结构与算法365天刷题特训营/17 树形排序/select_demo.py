# -*- coding: utf-8 -*-
import random

# 选择排序算法

N = 1000

nums = [random.randint(1, 99) for _ in range(N)]

nums2 = nums[:]


def select_sort(nums, index):

    if index == len(nums):
        return

    tail = nums[index + 1:]

    if not tail:
        return

    r = min(tail)

    j = nums.index(r, index + 1)

    nums[index], nums[j] = nums[j], nums[index]
    # print('kk', nums)

    select_sort(nums, index + 1)


print('before nums', nums)
select_sort(nums, 0)
print('after nums is', nums)

print('sorted(nums) == sorted(nums2)', sorted(nums) == sorted(nums2))
