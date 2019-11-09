# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        print('houses', houses)
        print('heaters', heaters)

        # 提前对供暖器进行排序操作
        heaters = sorted(heaters)
        n = len(heaters)
        max_v = 0
        for h_p in houses:
            le, ri = 0, n - 1
            res = float('inf')
            while le <= ri:
                mid = (le + ri) // 2
                v = heaters[mid]
                if v == h_p:
                   res = h_p
                   break
                elif h_p > v:
                    le = mid + 1
                else:
                    ri = mid - 1

            if le < n:
                res = min(res, heaters[le] - h_p)
            if ri >= 0:
                res = min(res, h_p - heaters[ri])

            max_v = max(max_v, res)

        return max_v

s = Solution()

houses = [1,2,3,4]
heaters = [1, 4]

r = s.findRadius(houses, heaters)
print(r)