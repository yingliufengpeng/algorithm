# -*- coding: utf-8 -*-

'''
    有n个人,每个人有各自的重量wi,每艘船的最大承载量均为C,且最多只能乘坐两个人.用最少的
    船装载所有人.

    贪心策略: 考虑最轻的人i,如果每个人都无法和他一起坐船(重量和超过C),则唯一的方案是每个人
    做一条船,否则,他应该选择和他一起坐船的最重的那个
'''

n = 10
nums = list(range(1, n + 1))

# step1 对重量进行排序的操作

nums_sort = sorted(nums)


def solve(nums, val):
    if not nums:
        return 0

    res = 0

    while nums:
        v = nums[0]
        j = len(nums) - 1
        while j > 0:
            v2 = nums[j]
            if v + v2 <= val:
                res += 1
                nums.pop(j)
                nums.pop(0)
                break

            j -= 1

        # 没有找到
        if j == 0:
            res += len(nums)
            break

    return res


print('sort of nums is', nums_sort)
r = solve(nums_sort, 10)

print('r is', r)

print('--' * 10)


def solve2(nums, val):
    if not nums:
        return 0

    cntPerson = len(nums)
    cntboat = 0

    p1 = 0
    p2 = len(nums) - 1

    while cntPerson > 0:
        if nums[p1] + nums[p2] > val:
            p2 -= 1
            cntPerson -= 1
            cntboat += 1

        else:
            p1 += 1
            p2 -= 1
            cntPerson -= 2
            cntboat += 1

    return cntboat


nums_sort2 = sorted(nums)
r2 = solve2(nums_sort2, 10)

print('r2 is', r2)
