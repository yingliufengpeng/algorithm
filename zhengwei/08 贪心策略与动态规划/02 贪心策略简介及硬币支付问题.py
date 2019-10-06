# -*- coding: utf-8 -*-

'''
    动态规划和贪心算法都是一种递推算法均用局部最优解来
    推导全局最优解

    是对遍历解空间的一种优化

    当问题具有最优子结构时,可用动态规划,而贪心是动态规划的特例
'''

'''
    有1元,5元,10元,50元,100元,500元的硬币各占c1, c5, c10, c50, c100, c500枚
    现在要用这些硬币来支付A元,最少需要多少枚硬币?
    
    贪心策略来解决 
    
    
    思路: 
        使用最少的那么就是尽量从最大的面额来使用
'''

coins = [1, 5, 10, 50, 100, 500]

num_coins = [3, 2, 1, 3, 0, 2]
num_coins2 = num_coins[:]

money = 618
money2 = 618

N = len(coins)

res = 0

# step1 迭代模式
for i in range(N - 1, -1, -1):
    # print('money is', money)

    v = coins[i]
    # print('v is', v)

    j = num_coins[i]

    count = j

    while j > 0 and money >= v:
        money -= v

        res += 1

        j -= 1

    # print('difference is', count - j)

    num_coins[i] = j

print('money is', money)
print('res is', res)
print('num_cons is', num_coins)


# 递归模式

def dfs(money, cur):
    if cur < 0:
        return 0

    # if money == 0:
    #     return 0

    max_value = coins[cur]

    t = money // max_value
    # print('t is', t)

    t = min(t, num_coins2[cur])

    # print('money {} max_value {} t {} nums_coins {}'.format(money, max_value, t, num_coins2[cur]))

    return t + dfs(money - max_value * t, cur - 1)


r = dfs(money2, N - 1)

print('r is', r)
