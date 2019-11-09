# -*- coding: utf-8 -*-


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sta, self.sta_min = [], []

    def push(self, x: int) -> None:
        self.sta.append(x)
        if not self.sta_min:
            self.sta_min.append(x)
        else:
            self.sta_min.append(min(self.sta_min[-1], x))

    def pop(self) -> None:
        self.sta.pop()
        self.sta_min.pop()

    def top(self) -> int:
        return self.sta[-1]

    def getMin(self) -> int:
        return self.sta_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(2)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#
# a = MinStack()
