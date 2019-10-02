# -*- coding: utf-8 -*-

'''
    给定一个N * N的矩阵matrix,在这个矩阵中,只有0和1两种值,返回边框全是1的最大正方形的边长长度
'''

# nums = [
#     [0, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1],
#     [0, 1, 0, 0, 1],
#     [0, 1, 1, 1, 1],
#     [0, 1, 0, 1, 1],
# ]


nums = [

    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
]

help_nums = [[[0]] * len(nums) for _ in range(len((nums)))]

print('help_nums is', help_nums)


def margin(nums, r, c, k) -> bool:
    if r + k >= len(nums) or c + k >= len(nums):
        return False

    else:
        for j in range(c, c + k + 1):

            if nums[r][j] == 0:
                return False

            if nums[r + k][j] == 0:
                return False

        for i in range(r, c + k + 1):

            if nums[i][c] == 0:
                return False

            if nums[i][c + k] == 0:
                return False

        return True


N = len(nums)
k = N - 1

res = False
r = c = 0
while k > 0:
    index = 0
    while index < N * N:
        r = index // N
        c = index % N
        res = margin(nums, r, c, k)
        index += 1

        if res:
            print('final k is', k)
            break

    if res:
        break

    k -= 1

if not res:
    print('没有该值')
else:

    print('有该值')
    print('k is', k)
    print('r c is {} {}'.format(r, c))

    print('边长为1的最大正方形的边长长度为: ', k + 1)
