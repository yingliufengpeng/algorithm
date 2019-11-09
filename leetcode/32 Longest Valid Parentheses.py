# -*- coding: utf-8 -*-

# 性质1 左括号一定对应有右括号
# 性质2 如果左括号为1,右括号为-1,那么括号的前缀和一定是>=0,括号的总和则一定是等于0
class Solution:
    def help(self, s):
        c = 0
        sta = 0
        max_v = 0
        i = 0
        while i < len(s):
            v = s[i]
            if v == '(':
                c += 1
            elif v == ')':
                c -= 1
            else:
                pass

            if c == 0:
                max_v = max(max_v, i - sta + 1)

            elif c > 0:
                pass

            else:
                sta = i + 1
                c = 0
            i += 1
        return max_v

    def longestValidParentheses(self, s: str) -> int:

        r1 = self.help(s)

        s2 = ''.join(['(' if e == ')' else ')' for e in reversed(s)])
        r2 = self.help(s2)
        # print(s2)
        # print(r1, r2)
        return max(r1, r2)


s = Solution()

str1 = "(()"

r = s.longestValidParentheses(str1)

print(r)
