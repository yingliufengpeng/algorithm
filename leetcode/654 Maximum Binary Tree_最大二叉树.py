# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
    单调栈的应用!!!
'''
from typing import List


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        # 使用递减单调栈
        sta = []
        for e in nums:
            new_node = TreeNode(e)
            while sta and e > sta[-1].val:
                node = sta.pop()
                new_node.left = node

            if sta:
                top_node = sta[-1]
                top_node.right = new_node

            sta.append(new_node)

        return sta[0]


s = Solution()
nums = [3, 2, 1, 6, 0, 5]
r = s.constructMaximumBinaryTree(nums)
print(r)
