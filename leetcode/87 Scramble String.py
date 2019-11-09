# -*- coding: utf-8 -*-

class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:

        def dfs(s1, s2):
            # 这步开始做剪枝的操作!!!
            if len(s1) != len(s2):
                return False
            if s1 == s2:
                return True

            n = len(s1)
            ss1 = ''.join(sorted(s1))
            ss2 = ''.join(sorted(s2))

            # 其实这步已经开始做剪枝的操作!!!
            if ss1 != ss2:
                return False

            for i in range(1, n):
                # print('s1[:i], s2[:i] s1[i:], s2[i:]', s1[:i], s2[:i], s1[i:], s2[i:])

                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    return True

                if dfs(s1[:i], s2[n - i:]) and dfs(s1[i:], s2[:n - i]):
                    return True

            return False

        return dfs(s1, s2)


s = Solution()

s1 = "abc"
s2 = "bca"
r = s.isScramble(s1, s2)
print('r is', r)
