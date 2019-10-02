# -*- coding: utf-8 -*-

'''
    给定一个矩阵matrix,其中的值有正,有负,有0,返回子矩阵的最大累加和

    eg:
        matrix = [
                [-1, -1, -1],
                [-1, 2, 2],
                [-1, -1, -1],
            ]
'''

from collections import defaultdict

matrix = [
    [-1, -1, -1],
    [-1, 2, 2],
    [-1, -1, -1],
]


def findmaxsubarray(nums):
    if not nums:
        return None

    max_v = nums[0]

    max_fianl = max_v

    N = len(nums)

    left = right = 0

    for i in range(1, N):

        if max_v >= 0:
            max_v += nums[i]

        else:
            max_v = nums[i]
            # 丢弃前部分和的同时,更新左指针
            left = i

        if max_v > max_fianl:
            max_fianl = max_v

            # 更新最大值的时候,更新右指针
            right = i

    return max_fianl, left, right


# beinrow = 0

N = len(matrix)
max_v = 0

for beginrow in range(N):

    # 每次都需要初始化该临时空间
    tmp = [0] * N

    for i in range(beginrow, N):
        row = matrix[i]
        # 按列进行累加
        for ii, v in enumerate(row):
            tmp[ii] += v

        r, _, _ = findmaxsubarray(tmp)

        if r > max_v:
            max_v = r

print('最大子数组的累加和为: ', max_v)
