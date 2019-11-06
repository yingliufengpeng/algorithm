# -*- coding: utf-8 -*-

'''
    题目描述
假设一个表达式有英文字母（小写）、运算符（+，—，*，/）和左右小（圆）括号构成，以“@”作为表达式的结束符。请编写一个程序检查表达式中的
左右圆括号是否匹配，若匹配，则返回“YES”；否则返回“NO”。表达式长度小于255，左圆括号少于20个。

输入格式
一行：表达式

输出格式
一行：“YES” 或“NO”
'''

s = '(25+x)*(a*(a+b+b)@'

sta = []

for e in s:

    if e == '(':

        sta.append(e)

    elif e == ')':

        if not sta:

            sta.append(e)

            break

        sta.pop()

    elif e == '@':

        break

    else:

        pass

# print(sta)

if sta:
    print('NO')
else:
    print('YES')