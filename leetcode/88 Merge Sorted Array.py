# -*- coding: utf-8 -*-
from typing import List

# 双指针的算法思路!!!
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1)
        i, j = m - 1, n - 1

        index = length - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1

            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        # print('i, j', i, j)
        while i >= 0:
            nums1[index] = nums1[i]
            i -= 1
            index -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            j -= 1
            index -= 1
        # print('i, j', i, j)
        print(nums1)


s = Solution()

nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1,2, 3]
n = 3

s.merge(nums1, 3, nums2, 3)
