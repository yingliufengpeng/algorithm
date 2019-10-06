# -*- coding: utf-8 -*-

'''
    如果一个字符串包含两个相邻的重复字串,则称它为容易的串,其它的串称之为困难的串,
    如:
        BB, ABCDACABCAB, ABCDABCD都是容易的, D, DC, ABDAB, CBABCBA都是困难的


'''


# 是否是一个困难串
def isHard(prefix, c):
    '''
        1: 遍历所有的长度为偶数的子串,看是否对称
        2: prefix本身是一个困难串
    :param prefix:
    :param c:
    :return:
    '''

    count = 0
    print('len of prefix is', len(prefix))
    for j in range(len(prefix) - 1, -1, -2):

        s1 = prefix[j: j + count + 1]
        s2 = prefix[j + count + 1:] + c

        if s1 == s2:
            return False

        count += 1

    return True


d = {
    'count': 0,
}


def dfs(strs, prefix):
    if d['count'] == 3:
        return

    # if prefix:
    #     print('prefix is', prefix)

    # 按照顺序进行处理,方便一些
    for e in strs:

        if isHard(prefix, e):
            d['count'] += 1
            dfs(strs, prefix + e)


strs = 'ABC'
dfs(strs, '')
