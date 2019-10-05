# -*- coding: utf-8 -*-


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


s = 'aabaabaab'

# 需要考虑到边界要处理的条件的思路
next_arr = next_of(s + ' ')

print('next_arr is', next_arr)


for i in range(2, len(next_arr)):

    k = next_arr[i]

    t = i - k

    if i % t == 0 and i // t > 1:

        print(i, ' ', i // t)
