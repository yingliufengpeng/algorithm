# -*- coding: utf-8 -*-

'''
    请实现一个算法,翻转一个给定的字符串.

    eg:
        "This is nowcoder!"
    output:
        !redocwon si sihT
'''


def reversestr(s):
    low = 0
    high = len(s) - 1

    s2 = [e for e in s]

    while low < high:
        s2[low], s2[high] = s2[high], s2[low]

        low += 1
        high -= 1

    return ''.join(s2)


s = "This is nowcoder!"

r = reversestr(s)

print('r is', r)
