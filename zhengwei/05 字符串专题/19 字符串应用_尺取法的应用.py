# -*- coding: utf-8 -*-


'''
    如果一个字符串恰好包含2个'h',1个'i'和1个'o', 我们就称这个字符串是hiho字符串

    现在给定一个只包含小写字母的字符串S,小Hi想知道S的所有子串中,最短的hiho字符串是
    哪个
'''

import sys


# 先检查是否是关键词
def check(c):
    return c == 'h' or c == 'i' or c == 'o'


# 是否包含所有的关键词
def containall(w, i, j):
    c1 = c2 = c3 = 0

    for e in w[i: j + 1]:

        if e == 'h':
            c1 += 1

        elif e == 'i':
            c2 += 1

        elif e == 'o':
            c3 += 1

        else:
            pass

    return c1 >= 2 and c2 >= 1 and c3 >= 1


# 是否恰好包含指定的关键字
def checkexact(w, i, j):
    c1 = c2 = c3 = 0

    for e in w[i: j + 1]:

        if e == 'h':
            c1 += 1

        elif e == 'i':
            c2 += 1

        elif e == 'o':
            c3 += 1

        else:
            pass

    return c1 == 2 and c2 == 1 and c3 == 1


def solve(w):
    # 初始化最小值
    min_v = sys.maxsize

    j = -1  # 用以遍历

    for i, c in enumerate(w):

        if check(c):  # i目前停下

            if j == -1:  # 只对j做一次定位
                j = i + 1

            while j < len(w):

                c2 = w[j]

                if check(c2) and containall(w, i, j):  # 先判断是否全部囊括

                    if checkexact(w, i, j) and j - i + 1 < min_v:
                        min_v = j - i + 1

                    # 只要进入到这个条件我们就停下
                    break

                j += 1

    print('res is', -1 if min_v == sys.maxsize else min_v)


S = 'hihofff'

solve(S)
