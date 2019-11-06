# -*- coding: utf-8 -*-

'''
    已知一颗二叉树的先序序列ABCECFG和中序序列DBEAFGC,画出这个二叉树
'''


class Node:

    def __init__(self, val):
        self.val = val

        self.left = self.right = None

    def __str__(self):
        return self.val

    def preorder(self) -> str:
        res = []

        def dfs(root):
            if root is None:
                res.append('#')
                return

            res.append(root.val)

            dfs(root.left)

            dfs(root.right)

        dfs(self)

        return ''.join(res)


pre_s = 'ABDECFG'

inor_s = 'DBEAFGC'


def create_node(pre_s, inor_s):

    if not pre_s:
        return None

    v = pre_s[0]

    root = Node(v)

    # print('prev, inors v', pre_s, inor_s, v)

    mid = inor_s.index(v)

    left = create_node(pre_s[1: mid + 1], inor_s[:mid])

    right = create_node(pre_s[mid + 1:], inor_s[mid + 1:])

    root.left = left

    root.right = right

    return root


root = create_node(pre_s, inor_s)

r = root.preorder()

print(r)