# -*- coding: utf-8 -*-

'''
    给定整数序列a1, a2, a3.. 判断是否可以从中选出若干,使它们的和恰为k

    深度优先搜索的逻辑

    # 做的逻辑则是通过非空子集的逻辑来做的思路
'''

from zhengwei.extra_python import subset_generate

# S = [1, 2, 3, 5, 6, 9, 10, 12, 14]

# 正常迭代的模式
S = list(range(5))

re = subset_generate.subset(S)

# print('re is', re)

k = 10

for vs in re:

    if sum(vs) == k:
        print('当前的值为:', vs)


# step2 通过递归模式来做相应的解决方案

def dfs(nums, cur, val, tmp_arr):
    if val == 0:
        print('获得结果 {} == {}'.format(k, tmp_arr))
        return

    if cur == len(nums) or val < 0:
        return

    v = nums[cur]
    tmp_arr |= {v}
    dfs(nums, cur + 1, val - v, tmp_arr)
    tmp_arr -= {v}
    dfs(nums, cur + 1, val, tmp_arr)


dfs(S, 0, 10, set())
