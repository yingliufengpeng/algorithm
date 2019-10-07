# -*- coding: utf-8 -*-

'''
问题描述
    有一个由非负整数组成的三角形，第一行只有一个数，除了最下行之外每个数的左下方和右下方各有一个数，从第一行的数开始，每次可以
    往左下和右下走一格，直到走到最下行，把沿途经过的数全部加起来，如何才能使这个和最大？？
'''

'''
    Description

            7
         3    8
       8    1    0
    2    7    4    4
  4    5    2    6   5

    (Figure 1)
Figure 1 shows a number triangle. Write a program that calculates the highest sum of numbers passed on a route that 
starts at the top and ends somewhere on the base. Each step can go either diagonally down to the left or diagonally 
down to the right. 


    Input

Your program is to read from standard input. The first line contains one integer N: the number of rows in the triangle. 
The following N lines describe the data of the triangle. The number of rows in the triangle is > 1 but <= 100. The 
numbers in the triangle, all integers, are between 0 and 99.
Output

Your program is to write to standard output. The highest sum is written as an integer.

    Sample Input
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5

    Sample Output
30
Source
'''
from collections import defaultdict
import copy


# 递归的模式解决
def dfs(nums, i, j):
    if 0 <= i < len(nums) and 0 <= j < len(nums[i]):
        t = nums[i][j]

        le = dfs(nums, i + 1, j)
        ri = dfs(nums, i + 1, j + 1)

        return t + max(le, ri)
    else:
        return 0


nums = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]

]

r = dfs(nums, 0, 0)

print('r is', r)


# 动态规划的模式解决

def solve(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0][0]

    c_nums = copy.deepcopy(nums)

    for i in range(len(c_nums) - 2, -1, -1):

        for j, v in enumerate(c_nums[i]):
            t1 = c_nums[i + 1][j]
            t2 = c_nums[i + 1][j + 1]
            t = c_nums[i][j] + max(t1, t2)
            c_nums[i][j] = t

    return c_nums[0][0]


r2 = solve(nums)

print('r2 is', r2)
