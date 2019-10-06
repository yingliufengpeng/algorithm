# -*- coding: utf-8 -*-

'''
    A group of N peoples wishes to go across a river with only one boat, which can at most carry two persons.
    Therefore some sort of shuttle(来回穿梭) arrangement must be arranged in order to row the boat back and forth
    so that all people may cross.
    Each person has a different rowing speed; the speed of a couple is determined by the speed of the slower
    one.
    Your job is to determine a strategy that minimizes the time for these people to get across.

Input
    The first line of the input contains a single integer T (1 <= T <= 20), the number of test cases.
    Then T cases follow.
    The first line of each case contains N, and the second line contains N integers giving the time for
        each people to cross the river.
    Each case is preceded by a blank line. There won't be more than 1000 people and nobody takes more than
        100 seconds to cross.

Output
    For each test case, print a line containing the total number of seconds required for all the N people
        to cross the river.

Sample Input

    1
    4
    1, 2, 5, 10

Sample Output

    17

'''


def min_cross_river(nums):
    res = 0

    # n = len(nums)
    print('nums is', nums)

    while True:
        n = len(nums)
        if len(nums) == 1:
            res += nums[0]
            break

        if len(nums) == 2:
            res += nums[1]
            break

        if len(nums) == 3:
            res += sum(nums)
            break

        # 策略,每次前2个人和后两个人进行互动
        # 这其中两种情况考虑
        # 1 前两个快的人带后面快的人
        # 2 第一个快的人带后面的人

        # 1,2 出发, 1返回,最后两名出发, 2返回
        t1 = nums[1] + nums[0] + nums[-1] + nums[1]

        # 1, 3出发, 1返回， 1, 4出发, 1返回
        t2 = nums[-1] + nums[0] + nums[-2] + nums[0]

        nums.pop()
        nums.pop()

        # print('t1, t2', t1, t2)
        res += min(t1, t2)
        n -= 2
    # print('res is', res)

    return res


nums = [1, 2, 2, 9]

res = min_cross_river(sorted(nums))

print('res is', res)