# -*- coding: utf-8 -*-

'''
    　假设我们有8种不同面值的硬币｛1，5，10，25｝，用这些硬币组合构成一个给定的数值n。 例如n=100，那么一种可能的组合方式为
     100 = 2*25+5*5+2*10+5*1。 问总共有多少种可能的组合方式？
'''
from collections import defaultdict
import copy

res = []


def dfs(nums, v, d):
    if v == 0:
        # 某种选择的模式
        if d not in res:
            res.append(copy.deepcopy(d))

        return

    if v < 0:
        return

    for n in nums:
        d[n] += 1
        dfs(nums, v - n, d)
        d[n] -= 1


nums = {1, 5, 10, 25}

d_dict = defaultdict(int)

r = []

dfs(nums, 6, d_dict)

# print('d_dict is', d_dict)


print('res is', res)

print('len of res is', len(res))
