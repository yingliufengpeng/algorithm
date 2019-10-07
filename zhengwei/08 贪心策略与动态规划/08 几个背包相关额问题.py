# -*- coding: utf-8 -*-

'''
    给出n个物体,第i个物体重量为wi, 选择尽量多的物体,使得总重量不超过C
    完全背包问题
'''

print('-' * 20)
Ws = [1, 1, 3, 4, 2, 4, 5, 6, 9]
print('WS is', Ws)

# 先对这些重量进行排序

Ws2 = sorted(Ws)
print('Ws2 is', Ws2)

N = len(Ws2)
index = 0
C = 10


def solve(nums, total):
    if not nums:
        return 0

    t = total
    i = 0

    while i < len(nums):

        if t >= nums[i]:
            t -= nums[i]
        else:
            break

        i += 1

    return i


r = solve(Ws2, 4)
print('r is', r)

'''
    部分背包问题
    
    有N个物体,第i个物体的重量为wi,价值为vi.总重量不超过C的情况下让总价值最高.
    每个物体都可以之取走一部分,价值和重量按比例计算.
    
    求最大总价值
    
    注意: 每个物体可以只拿一部分,因此一定可以让总重量恰好为C
'''

print('-' * 20)
Ps = [2, 3, 3, 4, 5]
Ws = [1, 2, 3, 4, 6]

# 计算每个物体的单价
unit_ps = [p / w for p, w in zip(Ps, Ws)]
print('unit_ps is', unit_ps)

P_pair3 = zip(Ps, Ws, unit_ps)


P_pair3_sort = sorted(P_pair3, key=lambda t: t[2], reverse=True)

print('P_pair3_sort is', P_pair3_sort)


def solve2(p_nums, val):
    if not p_nums:
        return 0

    index = 0
    price = 0

    while index < len(p_nums):

        v = p_nums[index][1]
        cur_p = p_nums[index][0]

        if v <= val:
            val -= v

            price += cur_p

        else:
            # 获得该重量的单价是多少
            unit_p = p_nums[index][2]
            price += val * unit_p

            break

        index += 1

    return price


r2 = solve2(P_pair3_sort, 2)

print('r2 is', r2)
