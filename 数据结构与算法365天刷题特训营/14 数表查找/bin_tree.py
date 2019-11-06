# -*- coding: utf-8 -*-


class Node:

    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __str__(self):
        return '{} {} {}'.format(self.left or '', self.val, self.right or '')

    def getrightmost(self):  # 树的最右子节点

        cur = last = self

        while cur.right:
            last = cur
            cur = cur.right

        return cur, last

    def serarch_val(self, val, parent):

        if self.val == val:
            return self, parent

        if self.left is None and self.right is None:
            return None, None

        v = self.val

        if self.right and val >= v:

            return self.right.serarch_val(val, self)

        elif self.left and val < v:

            return self.left.serarch_val(val, self)

        return None, None

    def delete_val(self, val):

        node, par_node = self.serarch_val(val, None)

        if node:

            if node.left and node.right is None:

                if par_node.left == node:

                    par_node.left = node.left

                else:

                    par_node.right = node.left

            elif node.right and node.left is None:

                if par_node.right == node:

                    par_node.right = node.right

                else:

                    par_node.left = node.right

            elif node.left is None and node.right is None:
                if par_node.left == node:

                    par_node.left = None

                else:
                    par_node.right = None


            else:

                node_2, par_node2 = node.left.getrightmost()

                if node_2 == par_node2:

                    if par_node.left == node:

                        par_node.left = node_2

                    else:

                        par_node.right = node_2

                else:

                    node.val = node_2.val

                    if par_node2.left == node_2:

                        par_node2.left = node_2.left

                    else:

                        par_node2.right = node_2.left


def bin_insert(root, val):
    if root is None:
        return Node(val)

    if root.left is None and val < root.val:
        root.left = Node(val)

        return root

    if root.right is None and val >= root.val:
        root.right = Node(val)

        return root

    if val > root.val:

        bin_insert(root.right, val)

    else:

        bin_insert(root.left, val)

    return root


def build_bin_tree(nums):
    r = None

    for e in nums:
        r = bin_insert(r, e)

    return r


nums = [25, 18, 69, 5, 20, 32, 30, 45]

root = build_bin_tree(nums)
print('builded tree is', root)

for e in nums[:-1]:
    print('root', root)
    root.delete_val(e)

# root.delete_val(25)
# root.delete_val(18)
