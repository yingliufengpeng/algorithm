# -*- coding: utf-8 -*-

'''
    题目描述
输入n个正整数，（1<=n<=10000),要求输出最长的连号的长度。（连号指从小到大连续自然数）

输入格式
第一行，一个数n;

第二行，n个正整数，之间用空格隔开。

输出格式
一个数，最长连号的个数。
'''

n_str = input('请输入一个数:')

n = int(n_str)

nums_str = input().split()

nums = [int(e) for e in nums_str]

max_v = 1
c = 1

for i in range(n):

    if i + 1 < n and nums[i] + 1 == nums[i + 1]:

        c += 1

    else:
        max_v = max(c, max_v)
        c = 1

print(max_v)
