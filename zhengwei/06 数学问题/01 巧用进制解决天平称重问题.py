# -*- coding: utf-8 -*-

'''
    用天平称重时,我们希望用尽量少的砝码组合秤出尽可能多的重量.
    如果有无限个砝码,但他们的重量分别是1, 3, 5, 9, 27, 81, ...
    等3的指数级神奇之处在于用它们的组合可以称出任意数量重量(砝码允许放在左右
    两个盘中)
'''


# 把实际值数转换为3进制
# 返回的数组是按照从低位到高位的顺序
def num2three(num, ba):
    cur = num

    res = []
    while cur > 0:
        t = cur % ba

        cur = cur // ba

        # res.insert(0, t)
        res.append(t)

    return res


# 本体使用的思路则是三进制的模式
r = num2three(10, 3)

print('r is', r)

# 有可能会越界,所以添加一位
r.append(0)

i = 0

while i < len(r) - 1:

    if r[i] == 2:
        r[i] = -1
        r[i + 1] += 1

    elif r[i] == 3:

        r[i] = 0
        r[i + 1] += 1

    else:
        pass

    i += 1

print('修改后的r is', r)

print('真正需要的结果为: ', list(reversed(r)))
