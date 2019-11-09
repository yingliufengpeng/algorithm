# -*- coding: utf-8 -*-

# 使用动态规划来解题
from typing import List
from collections import defaultdict


class Solution:

    # 动态规划版
    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:

        dp = defaultdict(list)

        dp[-1] = [[]]  # 启动一个空字符

        n = len(s)

        for i in range(0, n):
            r = []
            # 如果计算的dp[i]需要思考
            for word in wordDict:

                k = len(word)

                if i + 1 >= k:
                    # print('i is', i)
                    # print('s[i - k: i + 1] word', s[i - k: i + 1], word)
                    if s[i - k + 1: i + 1] == word:
                        # if i == 3:
                        #     print('word', word)

                        vs = dp[i - k]

                        r3 = [ss + [word] for ss in vs]

                        r.extend(r3)

            dp[i] = r or []

        # print('dp is', dp)

        res = []
        for vs in dp[i]:
            res.append(' '.join(vs))

        return res

    # 递归版 记忆化回溯
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dfs(w, words, visit):

            if w in visit:
                return visit[w]

            if not w:
                return [[]]

            res = []
            for word in words:
                k = len(word)
                if w.find(word) == 0:

                    rs = dfs(w[k:], words, visit)

                    r = []

                    for vs in rs:
                        r.append([word] + vs)
                    res.extend(r)
            visit[w] = res
            return res

        res = dfs(s, wordDict, {})
        r = [' '.join(vs) for vs in res]

        return r


so = Solution()
s = "aaaaaaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
r = so.wordBreak(s, wordDict)
print(r)
