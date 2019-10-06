# -*- coding: utf-8 -*-

'''
    你一定听说过“数独”游戏。
    如下图所示，玩家需要根据9×9盘面上的已知数字，推理出所有剩余空格的数字，并满足每一行、每一列、每一个同色九宫内的数字均含1-9，不重复。
    数独的答案都是唯一的，所以，多个解也称为无解。
    本图的数字据说是芬兰数学家花了3个月的时间设计出来的较难的题目。但对会使用计算机编程的你来说，恐怕易如反掌了。
    本题的要求就是输入数独题目，程序输出数独的唯一解。我们保证所有已知数据的格式都是合法的，并且题目有唯一的解。
    格式要求，输入9行，每行9个数字，0代表未知，其它数字为已知。
    输出9行，每行9个数字表示数独的解

'''


def check(table, r, c, v):
    for j in range(len(table)):
        if table[r][j] == v:
            return False

    for i in range(len(table)):

        if table[i][c] == v:
            return False

    rb = r // 3 * 3
    cb = c // 3 * 3

    for i in range(rb, rb + 3):
        for j in range(cb, cb + 3):

            if table[i][j] == v:
                return False

    return True


def dfs(table, r, c):
    index = r * len(table) + c
    if index == len(table) * len(table):
        print('table', table)
        return

    index += 1

    r2 = index // len(table)
    c2 = index % len(table)

    if table[r][c] == 0:  # 没有数字
        # 选择1-9之间合法的数字填到x, y这个位置

        for i in range(1, 10):
            if check(table, r, c, i):
                table[r][c] = i

                dfs(table, r2, c2)

                # 状态需要恢复  回溯
                table[r][c] = 0

            else:
                pass

    else:
        # 继续找下一个需要处理的位置
        dfs(table, r2, c2)


num_strs = [
    '005300000',
    '800000020',
    '070010500',
    '400005300',
    '010070006',
    '003200080',
    '060500009',
    '004000030',
    '000009700',
]

nums = [[int(e) for e in vs] for vs in num_strs]

# print('nums is', nums)

dfs(nums, 0, 0)
