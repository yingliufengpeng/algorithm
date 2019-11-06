# -*- coding: utf-8 -*-

from collections import defaultdict, namedtuple

# used用来判断该值是否已经判断过!!!
C_F = namedtuple('CharFreqency', ['val', 'frequency'])


class Node:

    def __init__(self, val, frequncy):
        self.val = val

        self.frequency = frequncy

        self.left = self.right = None

    def __str__(self):
        return '{}{}{}'.format(self.left or '', self.val, self.right or '')

    def encode(self):

        r = []

        if self.left is None and self.right is None:
            return [self.val]

        if self.left:

            les = self.left.encode()

        else:

            les = [[]]

        if self.right:

            ris = self.right.encode()

        else:

            ris = [[]]

        for vs in les:
            r.append('0' + vs)

        for vs in ris:
            r.append('1' + vs)

        return r

    # def encode(self):
    #     r = []
    #
    #     def dfs(root, prefix):
    #         if root.left is None and root.right is None:
    #             r.append(prefix + root.val)
    #             return
    #
    #         dfs(root.left, prefix + '0' + root.val)
    #
    #         dfs(root.right, prefix + '1' + root.val)
    #
    #     dfs(self, '')
    #     return r


char_frequency = [
    Node('a', 0.05),
    Node('b', 0.32),
    Node('c', 0.18),
    Node('d', 0.07),
    Node('e', 0.25),
    Node('f', 0.13),
]

# print('char_frequency', char_frequency)

r = sorted(char_frequency, key=lambda t: t.frequency)

# print('sorted of char_frequency is', r)

'''
    1: 选择没有双亲的节点(根据最小的两个节点)
    2: t1, t2作为左右子树构建一棵新树
    3: 新树的根的权值为t1和t2的和
'''

while len(char_frequency) >= 2:
    r = sorted(char_frequency, key=lambda tt: tt.frequency)

    t1, t2 = r[0], r[1]

    t = Node('', t1.frequency + t2.frequency)

    t.left = t1

    t.right = t2

    char_frequency = r[2:] + [t]

print('char_frequncy', char_frequency[0])

res = char_frequency[0].encode()

# ans = [''.join(str(e) for e in vs) for vs in res]

print('res', res)
