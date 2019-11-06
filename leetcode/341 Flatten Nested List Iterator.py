# -*- coding: utf-8 -*-
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        # self.n_list = nestedList

        self.index = 0

        self.cur = nestedList

        self.sta = []

        self.res = []

    def advance(self):

        if self.res:
            return

        v = None

        while True:
            if self.index == len(self.cur):
                if not self.sta:
                    # 说明堆栈已经为空
                    break
                else:
                    self.cur, self.index = self.sta.pop()
            else:
                t = self.cur[self.index]
                if isinstance(t, list):
                    self.sta.append((self.cur, self.index + 1))
                    self.cur = t
                    self.index = 0
                else:
                    self.index += 1
                    v = t
                    break
        self.res = [v]

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            t = self.res[0]

            self.res = []

            return t

    def hasNext(self):
        """
        :rtype: bool
        """

        self.advance()

        if self.res[0] is None:

            return False

        else:

            return True

# Your NestedIterator object will be instantiated and called as such:


nestedList = [[1, 1], 2, [1, 1]]

i, vs = NestedIterator(nestedList), []
while i.hasNext(): vs.append(i.next())
print(vs)
