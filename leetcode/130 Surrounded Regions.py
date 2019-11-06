# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        m = len(board)

        n = len(board[0])

        for i in range(m):
            for j in range(n):

                if board[i][j] == 'O':

                    sta = [(i, j)]
                    res = True
                    visit = set()
                    while sta:

                        r, c = sta.pop()

                        if (r == m - 1 or r == 0) and board[r][c] == 'O':
                            res = False

                        if (c == n - 1 or c == 0) and board[r][c] == 'O':
                            res = False

                        visit.add((r, c))

                        for d in directions:

                            rr, cc = r + d[0], c + d[1]

                            if 0 <= rr < m and 0 <= cc < n and (rr, cc) not in visit and board[rr][cc] == 'O':
                                visit.add((rr, cc))

                                sta.append((rr, cc))

                    for (r3, c3) in visit:
                        board[r3][c3] = res

        for i in range(m):
            for j in range(n):
                if board[i][j] is True:

                    board[i][j] = 'X'

                elif board[i][j] is False:
                    board[i][j] = 'O'
                else:
                    pass

        for line in board:
            print(line)


s = Solution()

board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
print('len of board is', len(board))
print('len of board[0] is', len(board[0]))
for line in board:
    print(line)
print('*' * 100)

import time

start = time.time()
s.solve(board)

end = time.time()

print("time duration is", end - start)
