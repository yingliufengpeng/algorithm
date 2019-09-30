# -*- coding: utf-8 -*-


'''

    思想则是使用快速排序的逻辑 在递归排序的过程中找到第k个元素的最小值
'''

nums = [1, 3, 4, 10, 2, 6]


# 分区的逻辑的确很重要的特性!!!
def partition(nums, low, high) -> int:
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

    # print('low, high is', low, high)
    nums[low], nums[high] = nums[high], nums[low]

    return high

'''

    最快效率的球乱序数组中的第k小的数,我们还是以快速排序为
    基本框架,然后在排序的过程中,mid值一定是第mid个最小值,所以以此
    作为基本条件对数据进行递归遍历的相关的操作
'''


def selectkK(nums, p, r, k):
    if k < 0:
        return None

    if k >= len(nums):
        return None

    q = partition(nums, p, r)
    qk = q - p + 1

    if qk == k:
        # print('qk is', qk)
        return nums[q]

    elif qk > k:
        # print('qk > k', qk, k)
        return selectkK(nums, p, q - 1, k)
    else:
        # print('qk > k', qk, k)
        return selectkK(nums, q + 1, r, k - qk)


print('nums is ', nums)

v = selectkK(nums, 0, len(nums) - 1, 4)

print('v is ', v)
