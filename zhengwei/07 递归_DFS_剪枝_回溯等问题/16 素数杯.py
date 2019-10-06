# -*- coding: utf-8 -*-

'''
    输入正整数N,对1 - N进行排列,使得相邻两个数之和均为素数,输出时从整数1开始,逆时针排列.同
    一个环恰好输出一次
'''

# 根据平方的角度来判断素数的关系
def isP(k):
    if k < 1:
        return False

    if k == 1:
        return True

    i = 2

    while i ** 2 <= k:
        if k % i == 0:
            return False
        i += 1
    return True


def check(tmp_nums, i, cur):
    if i in tmp_nums:
        return False

    return isP(tmp_nums[cur - 1] + i)


def dfs(tmp_nums, cur):  # 在此 nums大致也是可以不用使用到的
    # print('cur is', cur)

    if cur == len(tmp_nums):
        # print(tmp_nums)

        if isP(tmp_nums[0] + tmp_nums[-1]):
            print('ok', tmp_nums)

        return

    for i in range(2, len(tmp_nums) + 1):
        # 切记 cur代表着索引: 是从0这个位置开始的

        if check(tmp_nums, i, cur):
            # if i == 5:
            #     print(tmp_nums)
            #     print('cur is', cur)
            #     print('i', i)
            tmp_nums[cur] = i

            dfs(tmp_nums, cur + 1)

            # tmp_nums[cur] = 0  # 可以写到这个位置

        tmp_nums[cur] = 0       # 可以写到这个位置


N = 6

res = []

# nums = list(range(1, N + 1))

tmp = [0] * N

tmp[0] = 1

dfs(tmp, 1)
