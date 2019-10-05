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
p = 'ABA'

sub_fix = []

# 常规方法使用循环遍历获得后缀数组
for i in range(len(s)):
    # sub_fix.append(s[i:] + ' ' + str(i))
    sub_fix.append((s[i:], i))

print('sub_fix is', sub_fix)

# 对字符串进行排序,不过每个后缀字符串记录了该字符串的后缀索引
s2 = sorted(sub_fix)

# 获得排序后的后缀数组,以便于以后需要
print('soted sub_fix is', s2)

l = 0
r = len(s2) - 1


def compare(p, q):
    if p == q:
        return 0
    elif p > q:
        return 1
    else:
        return -1


while l <= r:

    mid = (l + r) // 2

    # 获取居中的后缀
    midsstr, index = s2[mid]

    res = None

    if len(midsstr) > len(p):
        midsstr = midsstr[0: len(p)]

    res = compare(midsstr, p)

    if res == 0:
        print('index is', index)

        break

    elif res < 0:
        l = mid + 1
    else:

        r = mid - 1
