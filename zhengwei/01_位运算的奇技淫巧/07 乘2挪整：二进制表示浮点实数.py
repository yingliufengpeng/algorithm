# -*- coding: utf-8 -*-

a = 0.5

res = []

index = 0
while a > 0:

    if index == 32:
        break


    a *= 2

    if a > 1:
        res.append(1)
        a -= 1

    else:
        res.append(0)

    index += 1

print('res ', '0.' + ''.join(str(i) for i in res))