# -*- coding: utf-8 -*-
from typing import List


# 这个题目则是使用递增单调栈
# 此题的思路是维护一个单调递增的栈


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        sta = [-1]  # 切记,-1的妙用在于如果当前的元素的左值不存在的时候正好可以用其作为代替
        max_v = 0
        for i, h in enumerate(heights):
            while sta[-1] != -1 and h < heights[sta[-1]]:
                cur_index = sta.pop()
                cur_hei = heights[cur_index]
                le_index = sta[-1]
                width = i - le_index - 1
                max_v = max(max_v, cur_hei * width)

            sta.append(i)

        while sta[-1] != -1:
            cur_index = sta.pop()
            cur_hei = heights[cur_index]
            le_index = sta[-1]
            width = n - le_index - 1
            max_v = max(max_v, cur_hei * width)

        return max_v


s = Solution()
nums = [2, 1, 2]
r = s.largestRectangleArea(nums)
print(r)
