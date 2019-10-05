# -*- coding: utf-8 -*-

'''
    走楼梯问题:
        变更, 有个小孩正在上楼梯, 楼梯有n阶台阶,小孩一次可以上1阶,2阶,3阶.请实现
        一个方法,计算小孩有多少种上楼的方式

        为了防止溢出,请将结果Mod 100000007

'''


# n阶走法的扩展思路

def recursion1(n):
    if n <= 0:
        return 0

    if n == 1 or n == 2:
        return n

    if n == 3:
        return 4

    return recursion1(n - 1) + recursion1(n - 2) + recursion1(n - 3)


n = 10
r = recursion1(n)

print('n is {} r is {}'.format(n, r))
