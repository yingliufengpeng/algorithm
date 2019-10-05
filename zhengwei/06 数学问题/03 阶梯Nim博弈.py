# -*- coding: utf-8 -*-

'''

    Nim经典数学问题的变体:
        Staircase Nim 游戏

    Georgia and Bob decide to paly a self-invented game. They draw a row of grids on paper, number
    the grids from left to right by 1, 2, 3..., and place N chessmen on different grids, as shown in
    the following figure for example


    Georgia and Bob move the chessmen in turn. Every time a player will choose a chessman, and move
    it to the left without going over any other chessman or across the left edge. The player freely
    choose number of steps the chessman moves, with the constraint that the chessman must be moved
    at least ONE step and one grid can at most contains ONE single chessman. The player who cannot
    make a move loses the game.


    Georgia always plays first since "Lady first". Suppose that Georgia and Bob both do their best
    in the game, ie... if one of them knows a way to win the game, he or she will be able to carry
    it out.

'''

'''
    切记,该方法目前为止并不是很理解!!!
'''


# nums代表着是nums[i]所对应的索引有chessman的意思
def deal(nums):
    # 先对数据进行相关的排序的操作
    nums = sorted(nums)

    res = 0

    n = len(nums)

    if n & 1 == 1:  # 代表奇数
        for i in range(0, n, 2):

            if i == 0:
                res ^= nums[i] - 1
            else:       # 6, 7 之间的没有空隙, （ 7 - 6 - 1） == 0是这个意思

                res ^= nums[i] - nums[i - 1] - 1

    else:  # 代表偶数

        for i in range(1, n, 2):
            res ^= nums[i] - nums[i - 1] - 1

    if res == 0:

        return 'Bob will win'
    else:

        return 'Georgia will win'


nums = [2, 3, 4, 5, 9]
r = deal(nums)

print('r is', r)
