# -*- coding: utf-8 -*-

'''
    有n项工作,每项工作分别在si时间开始,ti时间结束

    对于每项工作,你都可以选择参与与否,如果选择参与,那么自始至终都必须全程参与.
    此外,参与工作的时间不能重复(即使时开始时间的瞬间和结束时间的瞬间也是不允许重叠).
    你的目标是参与尽可能多的工作,那么最多能参与多少项工作呢?
'''

'''
    解决思路,总是选择结束的时间是最早的情况(依据经验的思路)
'''

from functools import cmp_to_key

nums_sta = [1, 2, 4, 6, 8]
nums_stop = [3, 5, 7, 9, 10]

# le为开始时间, ri为结束时间
t_pair = list(zip(nums_sta, nums_stop))


# 根据结束时间进行排序,如果结束时间相等,那么就用开始时间进行排序


def cmp(p1, p2):
    if p1[1] < p2[1]:

        return -1

    elif p1[1] == p2[1]:

        if p1[0] < p2[0]:
            return +1

        elif p1[0] == p2[0]:
            return 0

        else:
            return -1

    else:
        return +1


t_pair = sorted(t_pair, key=cmp_to_key(cmp))

print('nums_sta', nums_sta)
print('nums_stop', nums_stop)
print('nums_tpair', t_pair)


def getmaxjobs(p_nums):
    if not p_nums:
        return 0

    if len(p_nums) == 1:
        return 1

    min_time = p_nums[0][1]
    count = 1
    n = len(p_nums)
    i = 1
    while i < n:

        if p_nums[i][0] > min_time:
            min_time = p_nums[i][1]
            count += 1

        i += 1

    return count


res = getmaxjobs(t_pair)

print('res is', res)
