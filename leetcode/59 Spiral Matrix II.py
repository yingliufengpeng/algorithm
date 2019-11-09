# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        i = 1
        table = [[0] * n for _ in range(n)]
        k = -1

        r, c = 0, -1
        while True:
            # print('i is', i)
            if i == n ** 2 + 1:
                break

            k = (k + 1) % 4

            for _ in range(n):

                rr, cc = r + directions[k][0], c + directions[k][1]

                if 0 <= rr < n and 0 <= cc < n and table[rr][cc] == 0:
                    table[rr][cc] = i
                    i += 1
                    r, c = rr, cc
            # for line in table:
            #     print(line)
        return table


s = Solution()

r = s.generateMatrix(4)
for line in r:
    print(line)
