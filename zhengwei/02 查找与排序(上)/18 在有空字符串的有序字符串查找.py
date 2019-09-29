# -*- coding: utf-8 -*-

'''
    有个排序后的字符串数组,其中散布着一些空字符串,设计一个方法,找出给定字符串
    (肯定不是空字符串)的索引
'''
from typing import List

strs = ' ab c d ef gh '
print('len(strs) is ', len(strs))

print('strs is', strs)


def findchar(s: str, low: int, high: int, target: str) -> int:
    # if low >= high:
    #     return -1

    if low + 1 == high:
        return s[low: high + 1].find(target)

    mid = (low + high) // 2

    if s[mid] == target:
        # print('奇怪')
        return mid

    cur = mid

    print(' mid is ', mid)

    while cur <= high and s[cur] == ' ':
        cur += 1

    print('low cur high', low, cur, high)

    if cur == high + 1:
        return findchar(s, low, mid, target)
    else:

        v = s[cur]

        if target == v:
            return cur

        elif target >= v:

            return findchar(s, cur, high, target)
        else:

            return findchar(s, low, mid, target)


target = 'e'
r = findchar(strs, 0, len(strs) - 1, target)

print('r is ', r)

print('r index is ', strs.find(target))
