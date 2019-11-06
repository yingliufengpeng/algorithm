# -*- coding: utf-8 -*-

# fib(n) = fib(n - 1) + fib(n - 2)

# dp = {}
# #
# # dp[0], dp[1] = 0, 1
# #
# # for i in range(2, 100):
# #     dp[i] = dp[i - 1] + dp[i - 2]
# #
# # print('dp is', dp)

X, Y, P = 0, 1, 2

r = [
    [1, 2, 3],
    [3, 4, 4],
    [2, 4, 9],
]

for t in r:

    print('t[X], t[Y], t[P]', t[X], t[Y], t[P])
