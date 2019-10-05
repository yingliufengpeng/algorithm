# -*- coding: utf-8 -*-

'''
    全排列
'''




# 迭代版本

def permutation_linear(nums):
    if not nums:
        return

    res = [[nums[0]]]
    index = 1

    while index < len(nums):
        new_r = []
        for es in res:
            # print('es is', es)

            n = len(es) + 1

            for i in range(n):
                t = es[:]
                t.insert(i, nums[index])
                # print('t is', t)

                new_r.append(t)

        res = new_r

        index += 1

    t = map(lambda t: ''.join(str(e) for e in t), res)
    # print('t is', list(t))

    return list(t)


nums2 = 'ABCD'
r = permutation_linear(nums2)
print('r is', r)
print('len of r', len(r))
