# -*- coding: utf-8 -*-

'''
    有一个X * Y的网格,一个机器人智能走格点且只能向右或者向下走,要从左上角
    走到右下角

    请设计一个算法,计算机器人有多少种走法

    给定两个正整数x, y,请返回机器人走的走法数目.保证 x + y <= 12
'''

'''
    递归解法的确隐藏了很多的细节
    
    老板思维
'''


def solve(x, y):
    if x == 1 or y == 1:
        return 1

    return solve(x - 1, y) + solve(x, y - 1)


r = solve(4, 4)

print('r is', r)

'''
    打工者的思维
'''


def solve2(m, n):
    s = [[0] * (n + 1) for _ in range(m + 1)]

    # step1 初始头行边界
    # s[1] = [1] * (n + 1)

    for i, _ in enumerate(s[1]):
        s[1][i] = 1

    # step2 初始化头列边界
    for vs in s:
        vs[1] = 1

    print('s is', s)

    for i in range(2, m + 1):
        for j in range(2, n + 1):
            s[i][j] = s[i - 1][j] + s[i][j - 1]

    return s[m][n]


r = solve2(4, 4)

print('r is', r)
