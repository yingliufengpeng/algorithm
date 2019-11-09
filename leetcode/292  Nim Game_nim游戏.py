# -*- coding: utf-8 -*-

class Solution:
    def canWinNim(self, n: int) -> bool:

        res = []
        r = n % 3
        while n >= 3:

            n = n // 3

            res.append(3)

        if r != 0:
            res.append(r)

        print('res is', res)
        ss = 0
        for v in res:
            ss ^= v

        return ss != 0


s = Solution()

r = s.canWinNim(3)

print(r)
