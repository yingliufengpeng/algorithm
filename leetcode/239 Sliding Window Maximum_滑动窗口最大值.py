# -*- coding: utf-8 -*-
from typing import List
from collections import deque


# 滑动窗口最大值,单调递增队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        j = 0
        res = []
        for i, e in enumerate(nums):
            while que and e > nums[que[-1]]:
                que.pop()

            que.append(i)
            if que and i - j + 1 > k:
                if que[0] <= j: # 为什么等于零的目的在于我们的j已经更新到j + 1,所以之前的j不需要使用了
                    que.popleft()
                j += 1

            if que and i - j + 1 == k:
                res.append(nums[que[0]])

        return res


s = Solution()

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
r = s.maxSlidingWindow(nums, k)
print(r)
