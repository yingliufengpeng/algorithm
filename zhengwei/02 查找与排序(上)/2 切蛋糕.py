# -*- coding: utf-8 -*-


# 切蛋糕递归算法

def sum2(arr, index):

    if index == len(arr):
        return 0

    return arr[index] + sum2(arr, index + 1)


a = list(range(101))

print('a is', sum2(a, 0))


# 翻转字符串
a = 'abcd'

r = []
def revse(s, index):

    if index == -1:
        return
    # print(s[index])
    r.append(str(s[index]))
    revse(s, index - 1)

revse(a, len(a) - 1)
# r = revse(a, len(a) - 1)
print('revse a is', ''.join(r))