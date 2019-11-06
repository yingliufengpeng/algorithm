# -*- coding: utf-8 -*-

'''
    https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
'''
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)

        ]
        m = len(matrix)

        n = len(matrix[0])

        back = [[None] * n for _ in range(m)]

        max_v = float('-inf')


        def dfs(table, i, j):

            if back[i][j] is not None:
                return back[i][j]

            t = table[i][j]
            # print('t is', t)

            res = []

            for d in directions:

                r, c = i + d[0], j + d[1]

                if 0 <= r < m and 0 <= c < n and table[r][c] is not None and table[r][c] > table[i][j]:
                    table[i][j] = None

                    k = dfs(table, r, c)

                    res.append(k)

                    table[i][j] = t

            back[i][j] = max(res or [0]) + 1

            return back[i][j]

        for i in range(m):
            for j in range(n):

                if back[i][j] is not None:

                    max_v = max(max_v, back[i][j])

                else:

                    r = dfs(matrix, i, j)

                    max_v = max(max_v, r)

        # max_v = dfs(matrix, 0, 2)
        # print('back', back)
        return max_v


s = Solution()

matrix = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

ans = s.longestIncreasingPath(matrix)

print('r is', ans)
