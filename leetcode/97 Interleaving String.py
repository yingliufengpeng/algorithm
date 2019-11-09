# -*- coding: utf-8 -*-
'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

'''


from collections import defaultdict


# 进一步要理解dp递归方程的这句直接递推关系的意义
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False

        dp = defaultdict(bool)

        # dp[(i, j)] = (dp[(i - 1, j)] and s1[i] == s3[i - 1 + j]) or (dp[(i, j - 1)] and s2[j] == s3[i +  j - 1])
        # dp[(i, j)] 表示s1前一个字符,s2的前一个字符是否是s3的前i + j个字符
        # 初始化
        dp[(0, 0)] = True
        for i in range(1, m + 1):
            dp[(i, 0)] = dp[(i - 1, 0)] and s1[i - 1] == s3[i - 1 + 0]

        for j in range(1, n + 1):
            dp[(0, j)] = dp[(0, j - 1)] and s2[j - 1] == s3[0 + j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[(i, j)] = (dp[(i - 1, j)] and s1[i - 1] == s3[i - 1 + j]) or \
                             (dp[(i, j - 1)] and s2[j - 1] == s3[i + j - 1])

        # print('dp', dp)
        return dp[(m, n)]


s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
r = s.isInterleave(s1, s2, s3)
print(r)
