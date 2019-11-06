# -*- coding: utf-8 -*-

'''
    题目描述
输入一组勾股数a,b,c（a≠b≠c），用分数格式输出其较小锐角的正弦值。（要求约分。）

输入格式
一行，包含三个数，即勾股数a,b,c（无大小顺序）。

输出格式
一行，包含一个数，即较小锐角的正弦值
'''

nums_str = input().split()

nums = [int(e) for e in nums_str]

# 做排序的操作
nums.sort()

a, _, c = nums


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


mod = gcd(a, c)

print('{}/{}'.format(a // mod, c // mod))

# print('gcd(3, 4)', gcd(a, c))
