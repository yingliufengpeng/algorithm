# -*- coding: utf-8 -*-

'''
    动态规划方法代表了这一类问题(最优子结构or子问题的最优性)的一般解法,是设计方法或者策略,不是具体的算法

    本质是递推,核心是找到状态转移的方式,写出dp方程
'''

'''
    有N个重量和价值分别为wi, vi的物品,从这些物品中挑选出总重量不超过W的物品,求所有挑选方案中价值
    总和最大的值
    
    这类问题称之为0-1背包问题  
    递归模式的解决方案
'''

W = 7  # 承重的上限为W
p_w_nums = [  # (w, p) w为 重量, p为价格
    (2, 3),
    (1, 2),
    (3, 4),
    (2, 2),
]


# 可以通过子集生成的思路来思考的情况
# 备忘录的模式也是需要记录一些相关的函数处理过程的信息

def dfs(nums, index, W):
    # if W <= 0:
    #     return 0

    # if W == 0:
    #     return 0

    if index == len(nums):
        return 0

    v = nums[index][0]
    p = nums[index][1]

    t1 = t2 = 0

    if v > W:
        t2 = dfs(nums, index + 1, W)
    else:
        t1 = p + dfs(nums, index + 1, W - v)
        t2 = dfs(nums, index + 1, W)

    return max(t1, t2)


r = dfs(p_w_nums, 0, W)

print('r is', r)
