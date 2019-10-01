# -*- coding: utf-8 -*-


'''
    输入两个字符串str1和str2,请判断str1中的所有的字符是否包含在str2中

    使用python的集合的模式来处理该问题
'''


def contains(str1: str, str2: str) -> bool:
    s1 = set(str1)
    s2 = set(str2)

    return (s1 - s2) & s1 == set()


str1 = 'abddeg'
str2 = 'abcdeffgh'

print('res is', contains(str1, str2))
