# -*- coding: utf-8 -*-
from typing import List


# 单调栈的应用!!!
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sta = []
        d = {}
        for e in reversed(nums2):
            while sta and sta[-1] < e:
                sta.pop()
            d[e] = sta[-1] if sta else -1
            sta.append(e)

        print('d is', d)

        return [d[e] for e in nums1]


s = Solution()
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]

r = s.nextGreaterElement(nums1, nums2)
print(r)
