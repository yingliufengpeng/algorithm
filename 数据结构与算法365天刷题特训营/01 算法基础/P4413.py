# -*- coding: utf-8 -*-

'''
    题目描述
The number S is called the mean of two numbers R1 and R2 if S is equal to (R1+R2)/2. Mirko's birthday present for Slavko
 was two integers R1 and R2. Slavko promptly calculated their mean which also happened to be an integer but then lost R2!
  Help Slavko restore R2.

输入格式
The first and only line of input contains two integers R1 and S, both between -1000 and 1000.

输出格式
Output R2 on a single line.
'''

s = input().split()

r1 = int(s[0])

mean = int(s[1])

r2 = mean * 2 - r1

print(r2)
