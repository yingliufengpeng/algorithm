# -*- coding: utf-8 -*-

n_s = input('请输入一个正整数')

n = int(n_s)

a = n % 10

n //= 10

b = n % 10

n //= 10

c = n % 10


if n == a ** 2 + b ** 2 + c ** 2:
    print('是水仙花数')

else:
    print('不是水仙花数')
