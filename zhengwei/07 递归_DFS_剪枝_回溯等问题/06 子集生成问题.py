# -*- coding: utf-8 -*-

'''
    编写某个方法,返回集合的所有的子集

    给定
'''

import copy


# 递归模式

def getsubsetscore(s, index):
    if index == len(s):
        return [set()]
    #
    # if index == len(s) - 1:
    #     return [set(), {s[index]}]

    c = s[index]

    old_set = getsubsetscore(s, index + 1)
    new_set = []

    for o_set in old_set:
        # 对于每个子集,cur这个元素可以加进去,也可以不加进去
        new_set.append(o_set)

        clone_set = copy.deepcopy(o_set)
        # clone_set = o_set

        clone_set |= {c}

        new_set.append(clone_set)

    return new_set


s = 'ABCDEFGHIMNK'

r = getsubsetscore(s, 0)

print('r is', r)
print('len of r is', len(r))


def getsubsets(a):
    s2 = sorted(a)

    return getsubsetscore(s2, 0)

# 迭代的模式
