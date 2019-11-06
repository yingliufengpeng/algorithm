# -*- coding: utf-8 -*-

'''
    There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish
all courses?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 该题的解法则是通过拓扑排序的思路来展开
from typing import List

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 前驱课程指向后继课程
        d_post = defaultdict(set)

        # 后继课程指向前驱课程
        d_prev = defaultdict(set)

        for sta, end in prerequisites:
            d_post[end].add(sta)

            d_prev[sta].add(end)

        res = []
        while True:

            v = None
            for e in d_post:
                # 由于使用了python 中的collections中的方法,所以需要特别小心的处理
                if d_post[e] and not d_prev[e]:
                    v = e
                    break
            # print('v is', v)
            if v is None:
                break

            res.append(v)

            del d_post[v]

            for k in d_prev:
                d_prev[k] -= {v}

        print('d_post', d_post)
        print('d_prev', d_prev)
        return len(d_post) == 0


s = Solution()

n = 3
prerequisites = [[3, 1], [3, 2], [1, 0], [2, 0]]
r = s.canFinish(n, prerequisites)
print(r)
