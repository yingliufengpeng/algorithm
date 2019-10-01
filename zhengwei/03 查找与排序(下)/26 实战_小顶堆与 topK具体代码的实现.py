# -*- coding: utf-8 -*-

k = 5
glo_d = {
    'k': k,
    'heap': [0] * k,
    'size': 0,
}

print('heap is', glo_d['heap'])


# 目前我们使用数组来代表堆的使用


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


def deal(x):
    size = glo_d['size']
    k = glo_d['k']
    heap = glo_d['heap']
    if size < k:
        heap[size] = x
        size += 1
        glo_d['size'] = size

    # x和堆顶元素进行比较(最小堆)
    elif size == k:
        # 代码进行相关堆化
        minHeap(heap)
        size += 1
        glo_d['size'] = size

    # 由于是最小堆顶,所以比堆顶小的元素我们不需要去关注

    # x和堆顶进行比较,如果x大于堆顶,x将堆顶挤掉并向下调整
    size = glo_d['size']
    if size > k and heap[0] < x:
        heap[0] = x
        minheapfixdown(heap, 0, k)

    print('heap is ', heap)


for i in range(1, 10):
    deal(i)
