# -*- coding: utf-8 -*-

'''
    裴蜀公式

    对任何整数a,b和它们的最大公约数d,关于未知数x和y的线性丢番图方程(称为裴蜀公式)
    ax + by = m有整数解时当且仅当m是d的倍数

    裴蜀等式有无穷个整数解,每组解x, y都称之为裴蜀数,可用扩展欧几里得算法(Extended Euclidean algorithm)求得.


    a % b == a - ( a // b) * b

    gcd == b * x1 + (a - ( a // b) * b) * y1
        == b * x1 + a * y1 = (a // b) * b * y1
        == a * y1 + b * (x1 - a // b * y1)      (3)



    最终得出一个结论:

        x = y1
        y = x1 - a // b * y1

    # 注意:
    #     x1, y1是下一层

    通解:
        x = x0 + (b // gcd) * t
        y = y0 - (a // gcd) * t
'''

# 扩展的欧几里得
# 调用完成后x,y是ax + by = gcd(a, b)的解

d = {
    'x': 1,
    'y': 0,
}


def ext_gcd(a, b):
    if b == 0:
        d['x'] = 1
        d['y'] = 0

        return a

    res = ext_gcd(b, a % b)

    # x, y已经被下一层递归更新
    d['x'], d['y'] = d['y'], d['x'] - a // b * d['y']

    return res


ext_gcd(10, 4)

print('d is', d)
