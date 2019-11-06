# -*- coding: utf-8 -*-

'''
    相关的题目的信息
    https://leetcode-cn.com/problems/course-schedule-iii/
'''

from typing import List

from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if not prerequisites or not prerequisites[0]:
            return list(range(numCourses - 1, -1, -1))

        # 前驱课程指向后继课程
        d_post = defaultdict(set)

        # 后继课程指向前驱课程
        d_prev = defaultdict(set)

        for sta, end in prerequisites:
            d_post[end].add(sta)

            d_prev[sta].add(end)
        # print('d_post', d_post)
        # print('d_prev', d_prev)
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

        if len(d_post) == 0:
            return res + list(set(range(numCourses)) - set(res))
        return []


s = Solution()

n = 4
prerequisites = []
r = s.findOrder(n, prerequisites)
print(r)
