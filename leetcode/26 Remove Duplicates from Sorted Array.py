# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 1, 0 # 每次只关注i与i - 1是否相同
        n = len(nums)
        while i < n:
            if nums[i] == nums[j]:
                pass
            else:
                nums[j + 1] = nums[i]
                j += 1
            i += 1

        # print(nums)
        return j + 1

s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums = [1,1,2]
s.removeDuplicates(nums)
