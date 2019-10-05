# -*- coding: utf-8 -*-


'''
    变形词: 两个串有相同的字符及数量组成,

    给定两个字符串,请编写程序,确定一个字符串重新排列后,能否变成另一个字符串.

    这里规定大小写为不同的字符,且考虑字符串中的空格,


'''


def checksame(sa, sb):
    if len(sa) != len(sb):
        return False

    # step1 把字符转换成字符数组,然后进行相关排序的操作

    ssa = sorted(sa)
    ssb = sorted(sb)

    # step2 排序然后返回

    return ''.join(ssa) == ''.join(ssb)


r = checksame('abcd', 'dcab')

print('r is', r)
