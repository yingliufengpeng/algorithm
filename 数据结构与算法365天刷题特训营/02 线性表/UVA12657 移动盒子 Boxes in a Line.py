# -*- coding: utf-8 -*-

'''
    题意翻译
你有n个盒子在桌子上的一条线上从左到右编号为1……n。你的任务是模拟四种操作

1 X Y 移动盒子编号X到盒子编号Y的左边（如果X已经在Y的左边了就忽略）

2 X Y 移动盒子编号X到盒子编号Y的右边（如果X已经在Y的右边了就忽略）

3 X Y 交换盒子编号X与盒子编号Y的位置

4 将整条线反转

操作保证合法，X不等于Y

举一个例子，如果n=6，操作 1 1 4然后就变成了2 3 1 4 5 6；再操作 2 3 5就变成了 2 1 4 5 3 6；再操作 3 1 6 就变成 2 6 4 5 3 1；
最后操作4，就变成了 1 3 5 4 6 2

输入

最多有10组数据，每个数据会包含两个整数n,m（1≤n,m<100,000）, 接下来是m行数据，表示操作。

输出

对于每组数据，输出他们奇数位置的编号的和。
'''

# 本体使用静态链表的逻辑

n = 6

nums = list(range(n + 1))

nums_post = [e + 1 for e in nums]

nums_post[-1] = 0

num_prev = [e - 1 for e in nums]

num_prev[0] = 0

print('nums_prev', num_prev)

print('nums     ', nums)

print('nums_post', nums_post)


def show(nums, nums_prev, nums_post):
    print()
    print('nums_prev', nums_prev)
    print('nums     ', nums)
    print('nums_post', nums_post)


def command1(nums, nums_prev, nums_post, x, y):
    ix = nums.index(x)  # x的索引
    iy = nums.index(y)  # y的索引

    if nums_post[ix] == iy:
        return

    nums_post[nums_prev[ix]] = nums_post[ix]
    nums_prev[nums_post[ix]] = nums_prev[ix]

    nums_post[nums_prev[iy]] = ix
    nums_prev[ix] = nums_prev[iy]

    nums_post[ix] = iy
    nums_prev[iy] = ix

    show(nums, nums_prev, nums_post)


def command2(nums, nums_prev, nums_post, x, y):
    ix = nums.index(x)

    iy = nums.index(y)

    if nums_post[iy] == ix:
        return

    nums_post[nums_prev[ix]] = nums_post[ix]
    nums_prev[nums_post[ix]] = nums_prev[ix]

    nums_prev[nums_post[iy]] = ix
    nums_post[ix] = nums_post[iy]

    nums_prev[ix] = iy
    nums_post[iy] = ix

    show(nums, nums_prev, nums_post)


def command3(nums, nums_prev, nums_post, x, y):
    ix = nums.index(x)

    iy = nums.index(y)

    nums[ix], nums[iy] = nums[iy], nums[ix]

    show(nums, nums_prev, nums_post)


def command4(nums, nums_prev, nums_post):
    # print()
    n = len(nums)
    nums.reverse()

    nums_prev.reverse()

    nums_post.reverse()

    for i in range(n):
        nums_post[i] = n - nums_post[i] - 1
        nums_prev[i] = n - nums_prev[i] - 1

    show(nums, nums_prev, nums_post)


command1(nums, num_prev, nums_post, 1, 4)
command2(nums, num_prev, nums_post, 3, 5)
command3(nums, num_prev, nums_post, 1, 6)
# command4(nums, num_prev, nums_post)

# print('nums', nums)

c = 0

index = nums.index(0)

count = 0
while True:

    v = nums[index]

    index = nums_post[index]

    print(v)

    if index == 0:
        break
