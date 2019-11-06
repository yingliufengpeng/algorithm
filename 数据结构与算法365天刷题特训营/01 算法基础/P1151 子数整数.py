# -*- coding: utf-8 -*-

'''
    题目描述
对于一个五位数a_1a_2a_3a_4a_5a
1
​	 a
2
​	 a
3
​	 a
4
​	 a
5
​	 ，可将其拆分为三个子数：

sub_1=a_1a_2a_3sub
1
​	 =a
1
​	 a
2
​	 a
3
​

sub_2=a_2a_3a_4sub
2
​	 =a
2
​	 a
3
​	 a
4
​

sub_3=a_3a_4a_5sub
3
​	 =a
3
​	 a
4
​	 a
5
​

例如，五位数2020720207可以拆分成

sub_1=202sub
1
​	 =202

sub_2=020(=20)sub
2
​	 =020(=20)

sub_3=207sub
3
​	 =207

现在给定一个正整数KK，要求你编程求出1000010000到3000030000之间所有满足下述条件的五位数，
条件是这些五位数的三个子数sub_1,sub_2,sub_3sub
1
​	 ,sub
2
​	 ,sub
3
​	 都可被KK整除。

输入格式
一个正整数K

输出格式
每一行为一个满足条件的五位数，要求从小到大输出。不得重复输出或遗漏。如果无解，则输出“No”
'''

k_str = input()

k = int(k_str)

res = []

for n in range(1 * 10 ** 4, 3 * 10 ** 4 + 1):

    n_str = str(n)

    n1, n2, n3 = int(n_str[: 3]), int(n_str[1: 4]), int(n_str[2:])

    if n1 % k == 0 and n2 % k == 0 and n3 % k == 0:
        res.append(n)

if res:

    for e in res:
        print(e)
else:

    print('No')
