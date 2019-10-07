# -*- coding: utf-8 -*-
'''
    最长递增子序列的长度

    输入 4 2 3 1 5 6
    输出 3 (因为 2 3 5 组成最长递增子序列)
'''

from collections import defaultdict


def f(arr):
    maxcount = 0
    if not arr:
        return 0

    for i, _ in enumerate(arr):
        p = i
        cnt = 1
        for j in range(i + 1, len(arr)):

            if arr[j] > arr[p]:
                cnt += 1
                p = j

            maxcount = max(maxcount, cnt)
    return maxcount


nums = [4, 2, 3, 1, 5, 6, 2]

r = f(nums)

print('r is', r)


# 使用相关的动态规划的思维

def dp(nums):
    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    dp = defaultdict(int)

    dp[0] = 1

    for i in range(1, len(nums)):

        cnt = 1
        res = [1]   # 之所以加1 的目的在于我们的递归关系是必须以该元素为最后一个元素的结尾,所以最小为1
        for j in range(0, i):
            if nums[i] > nums[j]:
                # cnt = max(cnt, dp[j] + 1)
                res.append(dp[j] + 1)

        # dp[i] = cnt
        # print('res is', res)
        dp[i] = max(res)

    return max(dp.values())


r2 = dp(nums)

print('r2 is', r2)
