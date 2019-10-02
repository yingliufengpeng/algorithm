# -*- coding: utf-8 -*-

'''
    如果矩阵中某个元素为0,则将其所在的行和列清零
'''

nums = [

    [1, 3, 4, 0],
    [3, 0, 3, 5],
    [1, 3, 4, 4],
    [0, 3, 4, 3],
]

print('nums is', nums)


def clearzero2none(nums, i, j):
    if nums[i][j] == 0:

        for ii in range(len(nums)):
            # 列清零
            nums[i][ii] = None

            # 行清零
            nums[ii][j] = None


for i in range(len(nums)):
    for j in range(len(nums[i])):
        clearzero2none(nums, i, j)

print('after nums is', nums)

N = len(nums)

for i in range(N):
    for j in range(N):

        if nums[i][j] is None:
            nums[i][j] = 0

print('cleared None in nums is', nums)
