# -*- coding: utf-8 -*-

'''
Rod-cutting problem

    Given a rod of length n inches and a table of prices pi for i = 1,2,...,n,determine the maximum revenue
    rn obtainable by cutting up the rod and selling the pieces.

Example
    length i 1, 2, 3, 4,  5, 6,  7,  8,  9,  10
    price pi 1, 5, 8, 9, 10, 17, 17, 20, 24, 30


    动态规划算法通常基于一个递推公式及一个或多个初始状态。当前子问题的解将由上一个子问题的解推出。
    动态规划和分治法相似，都是通过分解，求解，并组合子问题来求解原问题。分治法将问题划分成相互独立互不相交的子问题，
    递归求解子问题，再将它们的解组合起来，求出原问题的解。与之相反，动态规划应用于子问题重叠的情况，即不同的子问题具有公共的子子问题。
    在这种情况下，分治算法会做出许多不必要的工作，它会反复的求解那些公共子子问题。而动态规划算法对每个子子问题只求解一次，将结果保存
    到表格（数组）中，从而无需每次求解一个子子问题都要重新计算。


    假定我们知道某公司出售一段长度为i英寸的钢条的价格为p[i](i=1,2,3….)
    钢条长度为整英寸如图给出价格表的描述（任意长度的钢条价格都有）


    rob_lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rob_prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
'''
from collections import defaultdict

rob_lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rob_prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# 这种则是递归解法
def cut_rod(nums, n):
    if n == 0:
        return 0

    r = []
    for i in range(n):
        r.append(nums[i] + cut_rod(nums, n - i - 1))

    return max(r)


N = len(rob_prices)
r = cut_rod(rob_prices, 5)

print('r is', r)

# 我们需要非递归解法
# 动态规划


dp = defaultdict(int)
dp[0] = 1

n = 5  # n <= N 才行
for i in range(1, n):
    # 很容易范迷糊,i则是代表着当前的n, rn = max(num[i] + r(n - i)
    r = []
    for j in range(i + 1):
        r.append(rob_prices[j] + dp[i - 1 - j])

    dp[i] = max(r)

print('r2 is', dp[n - 1])
# print('dp is', dp)
