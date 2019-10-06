# -*- coding: utf-8 -*-

import functools


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __gt__(self, other):        # >

        print('__ge__')

        print(self.score > other.score)

    def __le__(self, other):        # <=
        print('__le__')
        print(self.score < other.score)

    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0


s1 = Student('wang', 20)
s2 = Student('peng', 38)

# s = [s2, s1]
#
# print(s)
#
# s3 = sorted(s, reverse=True)
# print(s3)

s1 >= s2
s1 <= s2

s1 < s2
s1 > s2