# -*- coding: utf-8 -*-

'''
    求最大公共子序列问题(lcs)

    AB34C
    A1BC2
        结果为 ABC
'''

# step1 使用集合模式
s1 = '123'
s2 = '456'

s1_set = set(s1)
s2_set = set(s2)

print('res', s1_set & s2_set)

# 使用递归思路!!!(视频中有实现,本人没有实现)


# 使用动态规划
''' 
    代表当前范围内lcs的长度
         A B 3 4 C  
       A x
       1 
       B
       C
       2
'''

# 该方法以后有机会再看
