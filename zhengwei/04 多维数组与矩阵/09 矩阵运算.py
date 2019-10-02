# -*- coding: utf-8 -*-

'''
    矩阵运算的逻辑
'''

import copy

A = [
    [1, 2],
    [3, 4],
]

B = [
    [5, 6],
    [7, 8],
]

N = len(A)

# 矩阵相加

C = copy.deepcopy(A)

for i in range(N):
    for j in range(N):
        C[i][j] = 0

print('C is', C)

for i in range(N):
    for j in range(N):
        C[i][j] = A[i][j] + B[i][j]

print('矩阵A和B相加', C)

for i in range(N):
    for j in range(N):

        sum2 = 0

        for ii in range(N):
            sum2 += A[i][ii] * B[ii][j]

        C[i][j] = sum2

print('矩阵相乘后的结果', C)
