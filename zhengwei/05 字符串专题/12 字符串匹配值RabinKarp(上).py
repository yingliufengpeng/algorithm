# -*- coding: utf-8 -*-

'''
    求解搜索字符串的位置
    该RabinKarp要使用到hash相关的算法


'''


def myhash(s):
    hash2 = 0

    N = 31

    for e in s:
        hash2 = hash2 * N + ord(e)

    return hash2


def math(p, s) -> bool:
    '''

    :param p: 模式串
    :param s: 目标串
    :return: bool
    '''

    hash_p = myhash(p)

    k = len(p)

    res = False

    for i in range(len(s)):

        if i + k <= len(s):

            hash_i = myhash(s[i: i + k])

            if hash_i == hash_p:
                print('匹配成功!!!')
                res = True
                # return True

    return res


p = 'ABA'

s = 'ABABABA'

res = math(p, s)

print('res is', res)
