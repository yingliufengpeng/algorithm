# -*- coding: utf-8 -*-

# 通过python的list来进行顺序存储的逻辑

# 而且我们通过索引1的位置开始存储
# 如上所示0代表我们不存储任何值


# 小顶堆的下沉的操作

def sink(nums, k, n):

    while k * 2 <= n:

        m = le = k * 2  # 替换到下一个节点

        ri = le + 1

        if ri <= n and nums[ri] > nums[le]:

            m += 1

        if nums[k] < nums[m]:

            nums[k], nums[m] = nums[m], nums[k]

        k = m


def buildHeap(nums):

    n = len(nums) - 1

    k = n // 2

    while k > 0:

        sink(nums, k, n)

        k -= 1


def sort_heap(nums):

    n = len(nums) - 1

    k = n

    while k > 0:

        nums[1], nums[k] = nums[k], nums[1]

        sink(nums, 1, k - 1)

        # print('kkk', nums)

        k -= 1


nums = [None, 30, 28, 20, 16, 18, 2, 17, 6, 10, 12]

nums_bak = nums[:]

print('before nums', nums)

# step 1 build max_heap
buildHeap(nums)

print('builed nums is', nums)

# sort heap

sort_heap(nums)

print('sorted nums is', nums)

print('sorted nums == sort heapsort', sorted(nums_bak[1:]) == nums[1:])
