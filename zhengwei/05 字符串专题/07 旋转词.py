# -*- coding: utf-8 -*-

'''
    给定两个字符串s1和s2,要求判定s2是否能被通过s1做循环移位(rotate)得到的字符串所包含.
    eg:
        s1 = 'AABCD', s2 = 'CDAA', 返回True,
        s1 = 'ABCD', s2 = 'ACBD', 返回False



    该题道德解法: 可以看出对s1做循环移位(rotate)所得到的字符串将是字符串s1s1的子字符串.如果
    s2可以有s1循环移位(rotate)得到,那么s2一定在s1s1张.至此我们将问题转化成考察s2是否在s1s1
    上,可通过调用一次python中的 s1 + s1 得到函数的结果
'''

s1 = 'AABCD'
s2 = 'CDAA'

s = s1
N = len(s)
for i in range(N):
    a = s[: N - i - 1]
    b = s[N - i - 1:]

    c = b + a
    # print('c is', c)

res = s2 in s1 + s1

print('res is', res)
