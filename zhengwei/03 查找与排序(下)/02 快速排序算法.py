# -*- coding: utf-8 -*-

nums = list(range(9, -1, -1))

print('nums is ', nums)


# 分区的逻辑的确很重要的特性!!!
def partition(nums, low, high):
    '''
        一遍单向扫描法,定主元的情况
        该分区算法的逻辑是把第一个当做最大值来进行考虑,然后从中把最大的值放入到
        临界的那个位置中去
    :param nums:
    :param low:
    :param high:
    :return:
    '''

    if low + 1 == high:
        return low

    pivot = nums[low]
    index = low + 1

    while index <= high:  # 最终的边界条件为 high 指向到了倒出第一个小于pivot的数据,而index则是指向第一个大小pivot的数据
        if nums[index] <= pivot:
            index += 1
        else:
            nums[index], nums[high] = nums[high], nums[index]
            high -= 1

    print('low, high is', low, high)
    nums[low], nums[high] = nums[high], nums[low]

    return high


def partition2(nums, low, high):
    if low + 1 == high:
        return low

    p = nums[low]
    left = low + 1
    right = high
    while left <= right:
        # left 不停的往右走,直到遇到大于主元的元素
        while left <= right and nums[left] <= p:
            left += 1

        # right 一定是指向最后一个小于主元
        while left <= right and nums[right] > p:
            right -= 1

        # left == right 不需要进行元素的交换的逻辑
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    # while 退出时,两者交错,且right指向的是最后一个小于等于主元的位置,

    nums[low], nums[right] = nums[right], nums[low]

    return right


def quickSort(nums, low, high):
    if low >= high:
        return

    mid = partition2(nums, low, high)
    print('mid is', mid)

    quickSort(nums, low, mid - 1)
    quickSort(nums, mid + 1, high)


#
quickSort(nums, 0, len(nums) - 1)
print(nums)

# b = partition(nums, 0, len(nums) - 1)
#
# print('nums is ', nums)


b = [1, 2, 3, 4]
print('b is', b)
i = partition2(b, 0, len(b) - 1)
print('b is ', b)

print('i is ', i)
