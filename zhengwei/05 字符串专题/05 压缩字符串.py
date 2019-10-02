# -*- coding: utf-8 -*-


'''
    字符串连续出现的字符压缩成一个字符并在后面加上该字符的次数

    eg:
        s = 'aaabdd'
    output:
        r = 'a3b1d2'
'''

s = 'aaabddd'

r = []
last = s[0]
count = 1

for e in s[1:]:

    if last != e:
        r.append(last)
        r.append(str(count))
        last = e
        count = 1
    else:
        count += 1

else:
    r.append(last)
    r.append(str(count))

if len(r) > len(s):
    r = s

print('r is', ''.join(r))
