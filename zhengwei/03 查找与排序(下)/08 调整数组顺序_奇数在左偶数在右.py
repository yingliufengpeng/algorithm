# -*- coding: utf-8 -*-

nums = list(range(19, -1, -1))

print('nums is', nums)


def fn(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:

        while nums[low] % 2 != 0:
            low += 1

        while nums[high] % 2 != 1:
            high -= 1

        if low < high:
            nums[low], nums[high] = nums[high], nums[low]


fn(nums)

print('result of nums is', nums)
