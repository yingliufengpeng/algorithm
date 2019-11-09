# -*- coding: utf-8 -*-
from typing import List


# 现在看来是深度优先 + 前缀树的思路

# 1
# 把words中的word存入前缀树
# 2
# 对board进行深度优先搜索
# dfs三个核心部分：
# 1
# 新的字符不在搜索范围内，退出
# 2
# 新的字符在搜索范围内，且该字符与之前的字符串为words中的一个word, 加入结果集，并将word结束标志置0，放置重复搜索
# 3
# 按深度优先递归搜索


class Solution:

    # 现在看来是深度优先 + 前缀树的思路
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(table, i, j, t_node, s):
            ch = board[i][j]
            if ch not in t_node:
                return

            # 关键的一步在这里, t 是另个一个节点信息
            new_node = t_node[ch]
            if "end" in new_node and new_node["end"] == 1:
                res.append(s + ch)
                new_node["end"] = 0

            table[i][j] = "#"

            for d in directions:
                r, c = i + d[0], j + d[1]
                if 0 <= r < m and 0 <= c < n and table[r][c] != '#':
                    dfs(table, r, c, new_node, s + ch)

            table[i][j] = ch

        # 构建前缀树
        # 将word存入前缀树
        trie = {}
        for word in words:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t["end"] = 1
        # print(trie)

        m = len(board)
        n = len(board[0])
        res = []
        # 对board进行深度优先搜索
        for i in range(m):
            for j in range(n):
                dfs(board, i, j, trie, "")
        return res


s = Solution()
board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
         ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
         ["a", "a", "b", "a", "a", "b"]]
# words = ["bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
#          "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
#          "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
#          "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
#          "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
#          "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
#          "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
#          "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
#          "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
#          "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]

for line in board:
    print(line)

words = ['baabaaabaaba', "bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
         "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
         "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
         "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
         "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
         "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
         "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
         "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
         "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
         "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]

# words = ["oath","pea","eat","rain"]

res2 = s.findWords(board, words)

print('res2', res2)
