# -*- coding: utf-8 -*-
import random

# 基数排序

nums_lenght = 200

nums = [random.randint(0, 999) for _ in range(nums_lenght)]

# 排序的趟数

d = d_ori = len(str(max(nums)))

N = 10

buckets = [[] for _ in range(N)]

while d > 0:
    # print('d is', d)
    while nums:
        e = nums.pop()

        e2 = e // (10 ** (d_ori - d))

        remaing_k = e2 % 10

        buckets[remaing_k].append(e)

    # print('bucket is', buckets)

    nums = [e for vs in buckets for e in reversed(vs)]  # nums要重置

    buckets = [[] for _ in buckets]  # 这个桶也是需要重置!!!

    d -= 1

print('nums is', nums)

print('nums == sorted(nums)', nums == sorted(nums))
