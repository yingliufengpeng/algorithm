# -*- coding: utf-8 -*-

from collections import namedtuple

# 二叉树的创建

'''
    补空法,是指如果左子树或右子树为空时,则用特殊字符补空,如'#'.然后先按照先序遍历
    的顺序,得到先序遍历序列,根据该序列递归创建二叉树
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


def recer_create_tree(str, d={}) -> Node:
    index = d['index']

    d['index'] = index + 1

    if index == len(str):
        return None

    v = str[index]

    if v == '#':

        pass

    else:

        n = Node(v)

        left = recer_create_tree(str, d)

        right = recer_create_tree(str, d)

        n.left = left

        n.right = right

        return n


# def create_treel(root, s):
# #
# #     # root为当前的父节点
# #
# #     if not s:
# #
# #         pass
# #
# #     else:
# #
# #         n = Node(s[0])


rootA = Node('A')

rootB = Node('B')

rootC = Node('C')

rootD = Node('D')

rootE = Node('E')

rootF = Node('F')

rootG = Node('G')

rootA.left = rootB

rootA.right = rootC

rootB.left = rootD

rootB.right = rootE

rootC.left = rootF

rootF.right = rootG

r = rootA.preorder()

print('r is', r)

#
# print(rootA.right)

d = {
    'index': 0,
}
n = recer_create_tree(r, d)

print('n is', n.preorder())
