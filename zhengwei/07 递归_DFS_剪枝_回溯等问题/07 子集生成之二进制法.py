# -*- coding: utf-8 -*-


'''
    对子集的另一种解法,通过二进制的模式来解决
'''


def subset(strs):
    if not strs:
        return None

    n = len(strs)

    result = []

    # for i in range(2 ** n):
    for i in range(1 << n):

        r = bin(i)
        r = list(reversed(r))

        print('r is', r)

        res = set()
        for ii in range(n):

            if r[ii] == 'b':
                break

            if r[ii] == '1':
                res.add(strs[ii])

        result.append(res)

    return result


S2 = [chr(e) for e in range(ord('A'), ord('B') + 1)]

result = subset(S2)
print('result is', result)
print('len of result is', len(result))
