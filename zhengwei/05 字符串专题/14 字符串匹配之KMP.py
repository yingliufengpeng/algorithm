# -*- coding: utf-8 -*-

'''
    kmp目前这其中的设计的理论知识还不可知,以后需要加紧补充!!!
'''


# 使用方案求next相关的数组
def next_of(p):
    if not p:
        return -1

    # 临时使用的值
    next_d = [0] * len(p)
    if len(p) == 1:
        next_d[0] = -1
        return next_d

    next_d[0] = -1
    next_d[1] = 0

    j = 1
    k = next_d[j]

    while j < len(p) - 1:
        # print('k {} j {} k {} p[j] {} p[k] {}'.format(k, j, k, p[j], p[k]))

        # k < 0 则是代表着已经到达next数组的最前置的位置
        if k == -1 or p[j] == p[k]:

            k += 1
            j += 1
            next_d[j] = k
        else:
            k = next_d[k]

    return next_d


def indexofstr(s, p):
    if not s or not p:
        return -1

    if len(p) > len(s):
        return -1

    # 获得该p相关的next数组
    next_look = next_of(p)

    i = 0  # s的位置
    j = 0  # p的位置

    while i < len(s):

        # 1 如果j = -1,或者当前的字符串匹配成功(s[i] == p[j]),那么对i, j分别加1
        # j = -1,因为next[0] == -1,说明p的第一位和i这个位置无法匹配,这是i, j都增加1, j从0位开始
        if j == -1 or s[i] == p[j]:

            i += 1
            j += 1

        else:
            # 2 如果j != -1,且当前字符匹配失败(s[i] != p[j]),则i不变,j = next[j]
            # next[j]即为j所对应的next值
            j = next_look[j]

        if j == len(p):
            print('匹配成功!!!', i - j)
            break

        # i += 1


s = 'badbababbbbdd'
p = 'bababb'

indexofstr(s, p)
