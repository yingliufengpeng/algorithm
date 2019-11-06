# -*- coding: utf-8 -*-

'''
    题目描述
Given two integers A and B, A modulo B is the remainder when dividing A by B. For example,
the numbers 7, 14, 27 and 38 become 1, 2, 0 and 2, modulo 3. Write a program that accepts 10
numbers as input and outputs the number of distinct numbers in the input, if the numbers are
considered modulo 42.

输入格式
The input will contain 10 non-negative integers, each smaller than 1000, one per line.

输出格式
Output the number of distinct values when considered modulo 42 on a single line.
'''

# 其实要考虑的是桶排序的思路!!!
res = set()

for _ in range(10):

    r = input()

    res.add(int(r) % 42)

print(len(res))


