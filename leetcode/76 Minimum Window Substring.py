# -*- coding: utf-8 -*-

'''
    Given a string S and a string T, find the minimum window in S which will contain all the characters in
    T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import Counter, defaultdict

# 先从暴力解法看是否怎么去做!!!

class Solution:
    def minWindow2(self, s: str, t: str) -> str:

        if not s:
            return ""

        if len(s) < len(t):
            return ''

        ds = Counter(s)
        dt = Counter(t)



        def contain(ds, dt):

            # cs = Counter(s)
            # ct = Counter(t)

            cs = ds
            ct = dt

            # 只要是提前return的则是不满足条件,
            # 1 是 s中没有t中的元素
            # 2 是 s中的元素数量少于t中元素的数量
            for e in ct:

                if e not in cs:

                    return False

                if cs[e] < ct[e]:

                    return False

            return True

        k = len(t)  # 最小滑动窗口

        le = 0

        ri = k - 1

        low, high = 0, 0
        min_v = float('inf')

        res = ''

        # 初始化k个数据值

        ks = Counter(s[:k])

        while ri < len(s):

            # print('ri is', ri)

            while True:

                # print('1')

                if ri - le + 1 >= k:

                    if contain(ks, dt):

                        if ri - le + 1 < min_v:
                            min_v = ri - le + 1

                            # low, high = le, ri

                            res = s[le: ri + 1]

                        ks[s[le]] -= 1

                        le += 1

                    else:

                        break

                else:

                    break

            while True:

                # print('2')

                ri += 1

                if ri == len(s):
                    break

                ks[s[ri]] += 1

                # 只要当前已经存在有值了,我们就突出循环
                if contain(ks, dt):

                    if ri - le + 1 < min_v:
                        min_v = ri - le + 1

                        # low, high = le, ri

                        res = s[le: ri + 1]

                    break

        return res

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        dt = Counter(t)
        n = len(s)
        m = len(t)
        j = 0
        min_str = None
        tmp = defaultdict(int)
        for i in range(n):
            v = s[i]
            tmp[v] += 1

            while i - j + 1 >= m:
                flag = False
                for e in dt:
                    if dt[e] > tmp[e]:
                        flag = True
                        break
                if flag:
                    break
                # print(s[j - 1: i + 1])
                new_s = s[j: i + 1]
                if min_str:
                    if len(new_s) < len(min_str):
                        min_str = new_s
                else:
                    min_str = new_s

                tmp[s[j]] -= 1
                j += 1

        # print(tmp)
        return min_str or ''

s = Solution()

a = "a"

b = "aa"

c = 'BANC'

r = s.minWindow(a, b)

print('r is', r)
