# -*- coding: utf-8 -*-

'''
    将字符串单词翻转,如here you are翻转成are you here
'''


s = 'here you are'


r = ' '.join(list(s.split(' '))[::-1])

print('r is', r)
