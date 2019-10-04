# -*- coding: utf-8 -*-

'''
    求解搜索字符串的位置
    该RabinKarp要使用到hash相关的算法

    # 该哈希可能会产生冲突,所以有这些问题需要留意
'''
N = 31
import sys


def myhash(s):
    hash2 = 0
    for e in s:
        hash2 = hash2 * N + ord(e)

    return hash2


# step1 计算s长串hash值数组

# 用滚动的方法求出s中长度为n的每个子串的hash,组成一个hash数组
def myhash2(s: str, k: int) -> list:
    res = [0] * (len(s) - k + 1)

    # 先计算前k个字符的hash

    res[0] = myhash(s[0: k])

    for i in range(k, len(s)):
        new_char = s[i]
        old_char = s[i - k]
        v = (res[i - k] * N - N ** k * ord(old_char) + ord(new_char)) % sys.maxsize
        res[i - k + 1] = v

    return res


def match(p, s):
    hash_p = myhash(p)
    hash_s = myhash2(s, len(p))
    matchinner(hash_p, hash_s, p, s, len(p))


def matchinner(hash_p, hash_s, p, s, k):
    for i, h_s in enumerate(hash_s):

        if h_s == hash_p and s[i: i + k] == p:  # 可能会发生字符串的哈希值发生冲突,解决方法,再次验证s中的子串是否与匹配
            # 串p相同
            print('匹配!!,', i)


p = 'ABA'

s = 'ABABABA'

match(p, s)
