# -*- coding: utf-8 -*-

'''
    给定一个无序数组nums,求出需要排序的最短子数组长度

    要求:
        O(N)

    如输入:
        nums = [2, 3, 7, 5, 4, 6], 返回 4,因为只有[7, 5, 4, 6]需要排序

    以下的解法是通过升序的思路来做的操作,并不是很按照题目的要求去思考的!!!
'''
from typing import List

nums = [2, 3, 7, 5, 4, 6]

nums2 = [1, 2, 3, 4, 5, 6]

nums3 = [1, 5, 3, 4, 2, 6, 7]

nums4 = [2, 3, 7, 4, 1, 5, 6]


def findSegment(nums: List[int]) -> (int, int):
    n = len(nums)

    p1 = -1
    p2 = -1

    # 记录最大高点
    max_v = nums[0]
    min_v = nums[-1]
    # 拓展右端点, 只要右侧出现比历史最高低的,就应该扩展到此处
    for i, _ in enumerate(nums):

        # # 更新波峰
        # if i < n - 1 and nums[i] > nums[i + 1] and p1 == -1:
        #
        #     p1 = i

        # 只要当前值超越历史上的高峰,那么就需要做替换工作
        if nums[i] > max_v:
            max_v = nums[i]

        # 只要低于历史高峰,就要扩展排序区间的右端点
        if nums[i] < max_v:
            p2 = i

    # 找左端点: 更新历史最低点,只要左侧出现比历史最高的,就应该将左边界扩展到此处

    for i in range(n - 1, -1, -1):
        if nums[i] < min_v:
            min_v = nums[i]

        if nums[i] > min_v:
            p1 = i

    if p1 == -1:
        return -1, -1
    else:
        return p1, p2


p1, p2 = findSegment(nums4)

print('res is', nums4[p1: p2 + 1])
