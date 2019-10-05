# -*- coding: utf-8 -*-


'''
    对子集的另一种解法,通过二进制的模式来解决
'''

S = [chr(e) for e in range(ord('A'), ord('A') + 1)]

n = len(S)

result = []

for i in range(2 ** n):

    r = bin(i)
    r = list(reversed(r))
    # print('r is', r)

    res = set()
    for ii in range(n):

        if r[ii] == 'b':
            break

        if r[ii] == '1':
            res.add(S[ii])

    result.append(res)

print('result is', result)
print('len of result is', len(result))