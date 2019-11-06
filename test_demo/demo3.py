nums = list(range(1, 10))

indexs = list(range(9))

res = []


def dfs(nums, index):
    if index == len(nums):
        res.append(nums[:])

        # print(nums)

        return

    for i in range(index, len(nums)):
        nums[index], nums[i] = nums[i], nums[index]

        dfs(nums, index + 1)

        nums[index], nums[i] = nums[i], nums[index]


ans = []

dfs(indexs, 0)

pre_ans = [[nums[e] for e in vs] for vs in res]


# for line in pre_ans:
#
#     print(line)

# print(pre_ans)

def acc(nums):
    r = 0

    for e in nums:
        r = r * 10 + e

    return r


for vs in pre_ans:

    a, b, c = vs[:3], vs[3: 6], vs[6:]

    aa, bb, cc = acc(a), acc(b), acc(c)

    # print('aa {} bb {} cc {}'.format(aa, bb, cc))

    if bb == aa * 2 and cc == aa * 3:
        ans.append('{} {} {}'.format(aa, bb, cc))

ans.sort()

for vs in ans:
    print(vs)
