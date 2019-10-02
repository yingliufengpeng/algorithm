# -*- coding: utf-8 -*-

'''
    给定一个数组nums,返回子数组的最大累加和

    eg:
        nums = [1, -2, 3, 5, -2, 6, -1]

    out:
        因为 [3, 5, -2, 6] 最大的累加和为12
        所以返回 12
'''

# 一种解法: 其实这个问题使用的是动态规划的思想


nums = [1, -2, 3, 5, -2, 6, -1]
dp = {
    0: nums[0],
}
k = -1
for i in range(1, len(nums)):
    k = i

    dp[k] = max(nums[i], dp[k - 1] + nums[k])

print('dp is', dp)

res = max(dp.values())

print('res is', res)


# 使用另外一种解法
# 思路: 在加载的过程中,如果出现负数,就把当前的子数组清空,而不必需要,然后重新开始


def findmaxsubarray(nums):
    if not nums:
        return None

    max_v = nums[0]

    max_fianl = max_v

    N = len(nums)

    left = right = 0

    for i in range(1, N):

        if max_v >= 0:
            max_v += nums[i]

        else:
            max_v = nums[i]
            # 丢弃前部分和的同时,更新左指针
            left = i

        if max_v > max_fianl:
            max_fianl = max_v

            # 更新最大值的时候,更新右指针
            right = i

    return max_fianl, left, right


res2, le_index, ri_index = findmaxsubarray(nums)

print('res2 is', res2)
print('subarray is', nums[le_index: ri_index + 1])
