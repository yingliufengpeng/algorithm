# -*- coding: utf-8 -*-

'''
    区间选点问题

Intervals
    You are given n closed, integer intervals [ai, bi], and n integers c1..., cn.
    Write a program that:
        reads the number of intervals, their end points(两个端点) and integers c1, ..., cn from the standard input,
        computes the minimal size of a set Z of integers which has at least ci common elements with interval
        [ai, bi], for each i=1,2,...,n,
        write the answer to the standard output.

Input
    The first line of the input contains an integer n (1 <= n <= 50000) -- the number of intervals.
    The following n lines describe the intervals. The (i + 1)-th line of input contains three integers ai,
    bi, and ci separated by single spaces and such that 0 <= ai <= bi <= 50000 and 1 <= ci <= bi - ai + 1.

Output
    The output contains exactly one integer equal to the minimal size of set Z sharing at least ci elements
    with interval [ai, bi], fro each i=1,2,3,...,n.

Sample Input
    5
    3 7 3
    8 10 3
    6 8 1
    1 3 1
    10 11 1

Sample Output
    6


    解题思路:
        尽量选择靠右的点



    下面的解决方案效率上还是有些低,如果需要更高的方案,则是需要使用所谓的树状数组的数据结构,这个以后去理解!!!
'''


class Interval:

    def __init__(self, be, end, count):
        self.begin = be
        self.end = end
        self.count = count

    def __le__(self, other):
        return self.end <= other.end

    def __gt__(self, other):
        return self.end > other.end

    def __str__(self):
        return '({} {} {})'.format(self.begin, self.end, self.count)

    # __repr__ = __str__

    def __repr__(self):
        # print('__repr__')

        return self.__str__()


p_nums = [
    [3, 7, 3],
    [8, 10, 3],
    [6, 8, 1],
    [1, 3, 1],
    [10, 11, 1],

]

intervals = [Interval(s, e, v) for s, e, v in p_nums]

print('intervals is', intervals)

sorted_intervals = sorted(intervals)

print('sorted intervals is', sorted_intervals)

# min_val = sorted_intervals[0].end

n = len(sorted_intervals)
# min_interval = sorted_intervals[0]

print('n is', n)
i = 0

res = [0] * (sorted_intervals[-1].end + 1)

while i < n:

    e = sorted_intervals[i]

    count = e.count
    begin = e.begin
    while count > 0 and res[begin] == 1:

        begin += 1

        count -= 1

    end = e.end

    while count > 0:
        res[end] = 1
        end -= 1

        count -= 1

    i += 1

print('res is', res)

print('result is', sum(res))