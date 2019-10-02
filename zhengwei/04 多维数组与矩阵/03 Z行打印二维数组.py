# -*- coding: utf-8 -*-

'''
    Z形打印二维数组
'''

# nums = [
#
#     [1, 3, 4, 0],
#     [3, 0, 3, 5],
#     [1, 3, 4, 4],
#     [0, 3, 4, 3],
# ]

N = 4

nums = [list(range(i * N + 1, (i + 1) * N + 1)) for i in range(N)]

# N = len(nums)

for i in range(2 * N - 1):

    for ii in range(i + 1):

        if ii < N and i - ii < N:
            print(nums[i - ii][ii])
