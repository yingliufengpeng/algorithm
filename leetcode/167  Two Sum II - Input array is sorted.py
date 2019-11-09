# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = len(numbers) - 1
        for j in range(n - 1):

            # 不断地往前探视,只需要找到最近的nums[i] + nums[j] >= target
            while i - 1 > j and numbers[i - 1] + numbers[j] >= target:
                i -= 1

            if numbers[i] + numbers[j] == target:
                return [j + 1, i + 1]


s = Solution()
nums = [2, 7, 11, 15]
target = 9

r = s.twoSum(nums, target)

print(r)