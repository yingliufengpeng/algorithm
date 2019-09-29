# -*- coding: utf-8 -*-
import time
a = list(range(10 ** 8))


def binary_find(nums, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    elif target < nums[mid]:
        return binary_find(nums, low, mid - 1, target)

    else:
        return binary_find(nums, mid + 1, high, target)


start = time.time()
i = binary_find(a, 0, len(a) - 1, 7)

print('i is ', i)

print('time is ', time.time() - start)
