# -*- coding: utf-8 -*-

nums = [1, 1, 1, 3, 4, 5, 5, 6, 1, 1]

'''
    发帖王则是代表着该nums中有一多半的数据都是该人发布的
    比如上面的nums数据
'''


def solve(nums):
    if not nums:
        return

        # 默认第一个为候选数
    cadidate = nums[0]

    # 出现的次数,作进一步的累加的操作

    ntimes = 1

    # 扫描后面的数组

    for v in nums[:1]:
        # 两两消减为0,应该把现在的元素作为候选键
        if ntimes == 0:
            cadidate = v
            continue

        # 遇到候选键相同时,次数加1

        if v == cadidate:
            ntimes += 1
        else:
            ntimes -= 1

    print('cadidate is ', cadidate)


solve(nums)
