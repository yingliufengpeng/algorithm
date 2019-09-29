# -*- coding: utf-8 -*-

'''
    最长的递增子序列,该数组中部分有递增子序列的情况
'''

nums = [1, 9, 2, 5, 7, 3, 4, 6, 8, 0]

subs = []

index = 0
for i, e in enumerate(nums):

    if not subs:
        subs.append([i])

    else:

        if subs[-1][-1] < e:
            subs[-1].append(e)
        else:

            index = i
            subs.append([e])

print('max_subs', subs)

# 提前判断subs有值的情况

r = sorted(subs, key=lambda t: len(t), reverse=True)

print('r is ', r[0])
