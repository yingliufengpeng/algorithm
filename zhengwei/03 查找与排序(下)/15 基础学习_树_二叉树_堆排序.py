# -*- coding: utf-8 -*-

'''
    通过数组来存储二叉树的结构,然后前中后序遍历树
'''

nums = [0, 1, 2, 3, 4, 5, 6]


def previsit(nums, index):
    if index >= len(nums):
        return

    print('val is', nums[index])
    previsit(nums, index * 2 + 1)
    previsit(nums, index * 2 + 2)


def invisit(nums, index):
    if index >= len(nums):
        return

    invisit(nums, index * 2 + 1)
    print('val is ', nums[index])
    invisit(nums, index * 2 + 2)


def postvisit(nums, index):
    if index >= len(nums):
        return

    postvisit(nums, index * 2 + 1)
    postvisit(nums, index * 2 + 2)
    print('val is', nums[index])


print('*' * 10)
previsit(nums, 0)

print('*' * 10)
invisit(nums, 0)

print('*' * 10)
postvisit(nums, 0)