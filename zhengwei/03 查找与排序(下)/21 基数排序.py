# -*- coding: utf-8 -*-

N = 10
bucket = [[] for _ in range(10)]

glo_d = {
    'bucket': bucket,
}

print('bucket is', bucket)


# p则代表着该列中某个数字所处于哪个位置
# 将数组nums按照d个位进行分配和收集
def myradixsort(nums, p):
    bucket = glo_d['bucket']
    # print('myradixsort nums is', nums)
    for e in nums:
        m = (e // (10 ** (p - 1))) % 10

        bucket[m].append(e)

    index = 0
    for vs in bucket:

        for j in vs:

            nums[index] = j

            index += 1

    # res = []
    #
    # for bu in bucket:
    #     res.extend(bu)
    #
    # nums[:] = res[:]
    # print('myradixsort res is ', res)


def radixsort(nums):
    d = 1  # 入桶的位初始化为1

    max_v = max(nums)  # 获得最大值

    d_num = len('{}'.format(max_v))

    # d = d_num
    while d <= d_num:
        glo_d['bucket'] = [[] for _ in range(10)]
        myradixsort(nums, d)
        d += 1


nums = [1, 3, 4, 8, 10, 5, 3, 2, 2, 4, 10, 34]

print('prev nums is', nums)
radixsort(nums)

print('res nums is ', nums)
