# -*- coding: utf-8 -*-


'''
    为什么从 n // 2 - 1的位置来做后续处理,逻辑在于大于 n  // 2 - 1的索引值都在
    后面的位置的情况
'''
'''
    堆排序前提是对数据进行最小堆的堆化,然后对堆进行排序
'''


def minHeap(nums):
    for i in range(len(nums) // 2 - 1, -1, -1):
        minheapfixdown(nums, i, len(nums))


def minheapfixdown(nums, i, n):
    # 找到左右孩子
    le_index = i * 2 + 1
    ri_index = i * 2 + 2

    # 如果nums[i]比两个孩子都要小,不用做调整

    # if le_index >= len(nums):
    #     return

    if le_index >= n:
        return

    min_v = le_index
    # if ri_index >= len(nums):
    if ri_index >= n:
        pass
    else:
        if nums[ri_index] < nums[le_index]:
            min_v = ri_index

    if nums[i] <= nums[min_v]:
        return

    # 否则找到两个孩子中较小的,和i交换
    nums[i], nums[min_v] = nums[min_v], nums[i]

    # 小孩子那个位置的值发生了变化,i变更为小孩子那个位置,递归调整
    minheapfixdown(nums, min_v, n)


def mysort(nums):
    # 先对nums进行堆化
    minHeap(nums)

    # 把堆顶0号元素和最后一个元素进行对调
    for x in range(len(nums) - 1, -1, -1):
        nums[0], nums[x] = nums[x], nums[0]

        minheapfixdown(nums, 0, x - 1)

    # 缩小堆范围,对堆顶元素进行向下调整


nums = [5, 3, 6, 2, 8, 1, 9, 23]

print('nums is', nums)

# minHeap(nums)
mysort(nums)
print('result of nums is', nums)
