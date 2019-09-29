# -*- coding: utf-8 -*-

# 算法思路,所需要找的最小值一定是在无序的那段区间之中

a = list(range(4, 20))

a = a + [0, 1, 2, 3]
# a = [5, 6, 1, 2, 3]

print('a is', a)


def findMin(nums, low, high):

    # if low == high:
    #     return nums[low]

    if low + 1 == high:
        return min(nums[low], nums[high])

    mid = (low + high) // 2

    if nums[low] < nums[mid]:
        return findMin(nums, mid, high)

    else:
        return findMin(nums, low, mid)


r = findMin(a, 0, len(a) - 1)

print('r is', r)