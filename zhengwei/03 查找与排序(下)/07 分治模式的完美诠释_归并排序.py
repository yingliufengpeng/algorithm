# -*- coding: utf-8 -*-
from typing import List

nums1 = list(range(9, -1, -1))

# nums2 = list(range(14, 10, -1))

print('nums1 ', nums1)

# print('nums2 ', nums2)


def mergesort(nums1: List[int], nums2: List[int]) -> List[int]:
    if not nums1 or not nums2:  # nums1 == [] or nums2 == []
        return nums1 + nums2

    a, *ass = nums1
    b, *bss = nums2

    if a <= b:

        return [a] + mergesort(ass, nums2)

    else:

        return [b] + mergesort(nums1, bss)


# r = mergesort(nums1, nums2)
#
# print('r is ', r)

# 归并排序,最重要的则是对一半的数据进行排序的结果
'''
    归并排序(Merge Sort)算法完全依照分支模式
    
    分解: 将n个元素分成各含 n / 2 个元素的子序列
    解决: 对两个子序列递归进行排序
    合并: 合并两个已经排序的子序列以得到排序的结果
'''
def MergeSort(nums, p, r):
    if p >= r:
        return

    mid = (p + r) // 2

    MergeSort(nums, p, mid)
    MergeSort(nums, mid + 1, r)
    # print('nums xx is', nums)
    Merge(nums, p, mid, r)

    # MergeSort(nums, nums[:mid + 1], nums[mid + 1:])


def Merge(nums, p, mid, r):
    new_nums = nums[:]

    left = p  # 左侧队伍的头部指针,指向待比较的元素

    right = mid + 1  # 右侧队伍的头部指针,指向待比较的元素

    current = p  # 原数组指针,指向待填入数据的位置

    while left <= mid and right <= r:

        if new_nums[left] <= new_nums[right]:
            nums[current] = new_nums[left]
            current += 1
            left += 1
        else:
            nums[current] = new_nums[right]
            current += 1
            right += 1

    # 左边的指针可能没有到头,所以需要继续做填充
    while left <= mid:
        nums[current] = new_nums[left]
        current += 1
        left += 1

    # 右边的指针没有到头,但是我们可以不需要关注,
    # while right <= r:
    #     nums[right] = new_nums[right]
    #     current += 1
    #     right += 1

    # print('Merge nums is', nums)


MergeSort(nums1, 0, len(nums1) - 1)

print('nums1 is ', nums1)


# 以下则是测试用例

# nums2 = [1, 3, 2, 4]
#
# print('nums2 is', nums2)
# Merge(nums2, 0, (0 + len(nums2) - 1) // 2, len(nums2) - 1)
#
# # MergeSort(nums2, 0, len(nums2) - 1)
#
# print('nums2 is ', nums2)
