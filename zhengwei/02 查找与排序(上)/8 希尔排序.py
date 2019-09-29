# -*- coding: utf-8 -*-

a = list(range(10 ** 3, -1, -1))

print('希尔排序前 a is ', a)

interval = len(a) // 2

while interval > 0:
    i = 0
    while i < interval:
        for j in range(i + interval, len(a), interval):

            ii = j
            tmp = a[j]
            # 边界条件确实需要斟酌!!!
            while ii > i and a[ii - interval] > tmp:
                a[ii] = a[ii - interval]
                ii -= interval
            a[ii] = tmp

        i += 1
    interval //= 2

print('希尔排序后 a is ', a)
