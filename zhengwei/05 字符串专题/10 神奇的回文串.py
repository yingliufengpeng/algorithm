# -*- coding: utf-8 -*-

'''
    判断一个字符串是否为 回文字符串。
'''


s = 'abccba'

reverse_s = ''.join(reversed(s))

print('s is', s)
print('reverse of s is', reverse_s)

res = s == reverse_s

print('res is', res)