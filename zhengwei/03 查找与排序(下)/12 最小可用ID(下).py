# -*- coding: utf-8 -*-


''''
    在非负数组(乱序)中找到最小的可分配的id(从1开始编号),数量1 * (10 ** 3)

    不借助外部空间的做法

    对数据进行partition进行处理的模式 还是二分法查找,从中间下手,如果左侧紧密,
    那么nums[mid]

    假设nums是排序的,且是0,1,2,3---n这样的数值,那么在用二分法查找的时候,n // 2的
    位置的数据一定是 n // 2这个值,这是我们假设的情况
    另 mid = n // 2
    那么由此从这个角度出发,假设我们的数据是无序的,然后我们通过预期的mid与实际划分的
    位置q做比较,可得是否 q == mid + 1 来进行相关的比较的关系
'''


# nums = list(range(4, -1, -1))
# # nums.pop(2)
# # print('nums is', nums)

# nums = [1, 2, 3, 6, 8, 9, 10, 11]
# nums = [1, 2, 3, 4, 5, 8, 9, 10, 11, 1000]


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
    #  该条件的使用并不正确
    # if low + 1 == high:
    #     return low

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


def partition2(nums, low, high) -> int:
    '''
        一遍双向扫描,同时从左边和右边一起扫描
    :param nums:
    :param low:
    :param high:
    :return:  返回的值则是主元素所对应的索引值
    '''

    # 该条件的使用并不正确
    # if low + 1 == high:
    #     return low

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


def find4(nums, begin, end):
    if begin > end:
        return begin + 1

    mid = (begin + end) // 2

    t = mid + 1  # 期望值

    # 获得分区后的值,而不是索引值
    q = selectkK(nums, begin, end, mid - begin + 1)   # 调用查找第k大元素的方法

    if t == q:
        # 左侧紧密
        return find4(nums, mid + 1, end)
    else:
        # 左侧稀疏
        return find4(nums, begin, mid - 1)


nums = [1, 2, 3, 4, 5,  7, 8, 9, 10, 11]
print('-' * 100)
print('nums is ', nums)
r = find4(nums, 0, len(nums) - 1)

print('r is ', r)
