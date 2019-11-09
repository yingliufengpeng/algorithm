# -*- coding: utf-8 -*-
from typing import List

'''
    究竟为什么是这样的道理,以后得好好的想一想
'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: [-x[0], x[1]])
        print(people)
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


s = Solution()
p = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(p)
r = s.reconstructQueue(p)
print(r)