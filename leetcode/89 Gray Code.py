# -*- coding: utf-8 -*-
from typing import List

'''
    格雷编码
    00
    01
    11
    10  
    
    00
    10
    11
    01
        
    有n个位数,就会有2 ** n个编码方案!!!
'''


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res


s = Solution()

r = s.grayCode(2)
print(r)
