# -*- coding: utf-8 -*-

'''
    这类的方法是通过dynamic programming的模式

    有N个重量和价值分别为wi, vi的物品,从这些物品中挑选出总重量不超过W的物品,求所有挑选方案中价值
    总和最大的值



'''

'''
    f(x, y) = z 
    x: 由小到大选择物品个数,按序选择, eg x = 2. eg(x选择0, 1, 2这些数)
    y: 所选择的物品的重量,代表着一个值
    z: 代表着价格
    
    动态规划的解决方案
    python格式
    dp[(w, n)]:   w代表容量, n代表前物品的个数
    
'''

from collections import defaultdict


def solve(pair_nums, W):
    n = len(pair_nums)
    # print('n is', n)

    dp = defaultdict(int)

    # 构建表
    for i in range(n):
        for j in range(W + 1):
            dp[(i, j)] = 0

    # 初始化边界条件
    w = pair_nums[0][0]
    p = pair_nums[0][1]
    for i in range(W + 1):
        if w <= i:
            dp[(0, i)] = p

    # print('pr is', dp)

    for i in range(1, n):  # i代表着商品的个数
        for j in range(1, W + 1):  # j代表着商品的重量

            v = pair_nums[i][0]  # 重量
            p = pair_nums[i][1]  # 价格

            # print('v {} p {}'.format(v, p))

            if v <= j:
                dp[(i, j)] = max(p + dp[(i - 1, j - v)], dp[(i - 1, j)])
            else:
                dp[(i, j)] = dp[(i - 1, j)]

    # print('dp is', dp)

    return dp[(n - 1, W)]


W = 7  # 承重的上限为W
p_w_nums = [  # (w, p) w为 重量, p为价格
    (2, 3),
    (1, 2),
    (3, 4),
    (2, 2)
]

r = solve(p_w_nums, W)

print('r is', r)
