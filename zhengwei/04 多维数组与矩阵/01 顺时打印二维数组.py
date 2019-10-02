# -*- coding: utf-8 -*-

'''
    顺时针打印二维数组
'''

# nums = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]
# nums = [
#     list(range(1, 6)),
#     list(range(6, 11)),
#     list(range(11, 16)),
#     list(range(16, 21)),
#     list(range(21, 26)),
# ]

N = 5

nums = [list(range(i * N + 1, (i + 1) * N + 1)) for i in range(N)]

print('nums is', nums)

N = len(nums)
index = 0

while index < (N + 1) // 2:
    r = c = index  # 左上角
    r2 = c2 = N - 1 - index  # 右下角

    for j in range(r, r2 + 1):
        print(nums[r][j])

    for i in range(r + 1, r2 + 1):
        print(nums[i][c2])

    for j in range(c2 - 1, c - 1, -1):
        print(nums[r2][j])

    for i in range(r2 - 1, r, -1):
        print(nums[i][c])

    index += 1

