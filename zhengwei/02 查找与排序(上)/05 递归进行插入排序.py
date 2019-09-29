# -*- coding: utf-8 -*-

a = [1, 3, 4, 8, 9, 10, 2, 0, -1]


# 对数组进行递归排序
# 使用快排序
def recursive_sort(a, index):
    if index == len(a):
        return

    recursive_sort(a, index + 1)
    for i in range(index, len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]


recursive_sort(a, 0)

print('a is', a)
