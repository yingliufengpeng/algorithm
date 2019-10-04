# -*- coding: utf-8 -*-


'''
    什么是后缀数组
        就是串的所有后缀按字典排序后,排名和原下标的映射
        后缀数组就是:排名和原下标的映射,sa[0] = 5,起始下标为5的后缀 在所有
        后缀中字典序最小

        rank数组: 给定后缀的下标,返回其字典 序, rk[5] == 0

    后缀数组有什么用
        匹配

    怎么求后缀数组

    所谓的子串一定是某个后缀的前缀

'''

s = 'ABABABABB'

sub_fix = []

for i in range(len(s)):

    # sub_fix.append(s[i:] + ' ' + str(i))
    sub_fix.append((s[i:], i))

print('sub_fix is', sub_fix)

s2 = sorted(sub_fix)

print('soted sub_fix is', s2)