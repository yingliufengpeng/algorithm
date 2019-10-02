# -*- coding: utf-8 -*-


'''
    给定一个N * N的矩阵matrix,在这个矩阵中,只有0和1两种值,返回边框全是1的最大正方形的边长长度
'''
import copy

# nums = [
#     [0, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1],
#     [0, 1, 0, 0, 1],
#     [0, 1, 1, 1, 1],
#     [0, 1, 0, 1, 1],
# ]

nums = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
]

# nums = [
#     [1, 0],
#     [0, 1],
# ]

# 切记, 浅拷贝会导致符号会引用同一份的数据,所以使用深拷贝
nums_helper = copy.deepcopy(nums)

for i, vs in enumerate(nums_helper):
    for j, _ in enumerate(vs):
        vs[j] = [0, 0]  # 先右后下的思路

print('num_helper is', nums_helper)

N = len(nums)


def visit(nums, r, c):
    nums_helper[r][c] = 1
    if r + 1 >= N or c + 1 >= N:
        return 0

    ri = visit(nums, r, c + 1)
    do = visit(nums, r + 1, c)

    nums_helper[r][c] += ri + do

    return nums_helper[r][c]


index = N * N - 1

while index >= 0:
    r = index // N
    c = index % N
    # print('r c is {}, {}'.format(r, c))
    # print('nums[{}][{}] is {}'.format(r, c, nums[r][c]))
    if nums[r][c] == 1:
        j = c
        while j < N and nums[r][j] == 1:
            j += 1
        ri = j - c

        i = r
        while i < N and nums[i][c] == 1:
            i += 1
        do = i - r

        # print('ri do is {} {}'.format(ri, do))
        nums_helper[r][c] = [ri, do]

    # print('index is', index)
    index -= 1

print('nums_helper is', nums_helper)


def check(nums_helper, r, c, n):
    '''
        首先检测在(r, c)行列坐标中
        (r, c)位置的右方和下方同时大于等于n
        同时(r + n, c)的右方也要大于等于n
        同时(r, c + n)的下方也要大于等于n
    '''

    if nums_helper[r][c][0] >= n and nums_helper[r][c][1] >= n \
            and nums_helper[r + n - 1][c][0] >= n and nums_helper[r][c + n - 1][1] >= n:

        return True

    else:

        return False


k = N - 1
res = False
r = c = 0
while k > 0:
    for i in range(N):
        for j in range(N):
            res = check(nums_helper, i, j, k)
            if res:
                print('curi {} curj {} curk {}'.format(i, j, k))
                r, c = i, j
                break
        if res:
            break
    if res:
        break
    k -= 1

if k == 0:
    print(0)

else:
    print(k)
    print('r, c is {} {}'.format(r, c))
