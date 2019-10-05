# -*- coding: utf-8 -*-

res = []


def permutation(nums, index):
    if index == len(nums):
        r = nums[:]
        r = ''.join(str(e) for e in r)
        res.append(r)
        # res.append(nums)
        return

    for j in range(index, len(nums)):
        nums[index], nums[j] = nums[j], nums[index]

        permutation(nums, index + 1)

        nums[index], nums[j] = nums[j], nums[index]


nums = ['A', 'B', 'C', 'D']

permutation(nums, 0)

print('res is', res)
print('len of res is', len(res))