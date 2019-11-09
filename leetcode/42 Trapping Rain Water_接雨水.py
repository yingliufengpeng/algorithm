# -*- coding: utf-8 -*-
from typing import List

"""
此题的一种解法则是单调队列的解法

还有一种解法则是通过双指针的逻辑
    解法: 根据柱子的最高点把柱子分成两部分
"""


class Solution:

    # 解法一 双指针法
    def trap2(self, height: List[int]) -> int:
        if not height:
            return 0
        # step 1 找到最高的柱子,分成两半
        max_val = max(height)
        max_index = height.index(max_val)
        area = 0

        left_height = 0
        for i in range(max_index):
            if left_height < height[i]:
                left_height = height[i]
            else:
                area += left_height - height[i]
        right_height = 0
        for j in range(len(height) - 1, max_index, -1):
            if right_height < height[j]:
                right_height = height[j]
            else:
                area += right_height - height[j]

        return area

    # 解法二 栈思路
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        area = 0
        sta = []  # 入栈的元素是下标
        for i, h in enumerate(height):
            while sta and h > height[sta[-1]]:
                cur_index = sta.pop()
                cur_height = height[cur_index]
                if sta:
                    left_index = sta[-1]
                    left_height = height[left_index]
                    min_v = min(left_height, h)
                    area += (min_v - cur_height) * (i - left_index - 1)
                    print('area', area)
                else:
                    pass
            sta.append(i)
        return area


s = Solution()

nums = [4, 2, 0, 3, 2, 5]
r = s.trap(nums)
print(r)
