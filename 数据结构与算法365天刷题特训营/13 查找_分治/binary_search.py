# -*- coding: utf-8 -*-

nums = list(range(100))

le = 0

ri = len(nums) - 1

t = 33

while le <= ri:

    mid = (le + ri) // 2

    v = nums[mid]

    if v == t:

        print('find value')

        break

    elif v > t:

        ri = mid - 1

    else:

        le = mid + 1

