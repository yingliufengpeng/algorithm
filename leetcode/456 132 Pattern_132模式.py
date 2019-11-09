# -*- coding: utf-8 -*-

'''
    思路为单调递减队列队列
'''
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        sta = []
        s3 = float('-inf')
        for e in reversed(nums):
            if e < s3:
                return True
            while sta and e > sta[-1]:
                t = sta.pop()
                s3 = max(s3, t) # 更新次大值的逻辑!!!
            sta.append(e)

        return False
