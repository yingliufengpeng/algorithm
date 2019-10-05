# -*- coding: utf-8 -*-

'''
    全排列前缀递归法则
'''

res = []
def permutation(nums, perfix):
    if len(perfix) == len(nums):
        # print('perfix is', perfix)
        res.append(perfix)
        return

    for e in nums:
        cur = str(e)
        if cur not in perfix:
            permutation(nums, perfix + str(cur))


nums = [1, 2, 3, 4]
permutation(nums, '')
print('res is', res)
print('len of res is', len(res))