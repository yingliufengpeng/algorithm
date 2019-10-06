# -*- coding: utf-8 -*-

'''
    水洼数目

    有一个N x M大的园子, 雨后积来了水. 八连通的积水被认为是连接在一起的.
    强求出园子里总共有多少水洼?(八连通指的是下图中相对 W 的*的部分)

    关于八连通的思路的题!!!

    * * *
    * W *
    * * *

    限制条件:
    N, M <= 100

'''


def visit(table, x, y):
    M = len(table)
    N = len(table[0])

    r = x - 1
    c = y - 1

    r2 = x + 1
    c2 = y + 1

    for i in range(r, r2 + 1):
        for j in range(c, c2 + 1):

            if 0 <= i < M and 0 <= j < N:
                # print('i , j is', i, j)

                if table[i][j] == 'W':

                    table[i][j] = '.'
                    visit(table, i, j)
                else:

                    pass

            else:
                pass


s = """
    W........WW.
    .WWW.....WWW
    ....WW...WW.
    .........WW.
    .........W..
    ..W......W..
    .W.W.....WW.
    W.W.W.....W.
    .W.W......W.
    ..W.......W.
"""

r = s.strip().replace(' ', '').split('\n')

table = [[e for e in vs] for vs in r]
for vs in table:
    print(vs)

index = 0

M = len(table)
N = len(table[0])

count = 0

while index < M * N:

    r = index // N
    c = index % N

    if table[r][c] == 'W':
        count += 1
        visit(table, r, c)
        print('-' * 30)
        for vs in table:
            print(vs)



    index += 1

print('count is', count)

#
# visit(table, 0,  0)
# for vs in table:
#     print(vs)