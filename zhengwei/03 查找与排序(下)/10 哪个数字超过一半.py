# -*- coding: utf-8 -*-


nums = [1, 2, 3, 8, 8, 8, 8, 7, 8, 8]

''''

    只要排序之后,中间的数一定是最多出现的那个数字
'''

# step1 直接排序

r = sorted(nums)
print('res is ', r[-1])

# step2 哈希排序

pass


# step3 使用09章节中快速求出乱序数组中的第k小的数的算法

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

    # 该条件的使用并不正确
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


# r = selectkK(nums, 0, len(nums) - 1, len(nums) // 2)
#
# print('r is', r)


# step4 对于不同的数字进行消除的操作

s = [nums[0]]

for e in nums[1:]:
    if e != s[-1]:
        s.pop()
        s.append(e)
    else:
        break

print(s)
