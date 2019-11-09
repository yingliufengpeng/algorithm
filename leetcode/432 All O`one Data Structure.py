# -*- coding: utf-8 -*-
from collections import defaultdict


class LinkNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1  # 初始化默认就是1值
        self.next = self.prev = None

    def __str__(self):
        return 'instance {} {}'.format(self.key, self.val)

    __repr__ = __str__


class LinkList:

    def __init__(self):
        self.count = 0
        self.next = self.prev = None

        head = self.head = LinkNode(None, None)
        tail = self.tail = LinkNode(None, None)

        head.next = tail
        tail.prev = head

    def addFirst(self, node: LinkNode):
        nex = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nex
        nex.prev = node
        self.count += 1

    def removeLast(self):
        node = self.tail.prev
        prev = node.prev
        prev.next = self.tail
        self.tail.prev = prev
        node.prev = node.next = None
        self.count -= 1

    def popNode(self, node: LinkNode):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev
        node.next = node.prev = None
        self.count -= 1


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        # self.count_key = defaultdict(LinkList)
        self.count_key = {}
        # self.count_key = []  # 下标作为key [1, 2, 3, 4, ..]开始

        self.linkHead = LinkList()
        self.linkTail = LinkList()

        self.linkHead.next = self.linkTail
        self.linkTail.prev = self.linkHead

    def addLast(self, linknode: LinkList):

        prev = self.linkTail.prev
        prev.next = linknode
        linknode.prev = prev
        linknode.next = self.linkTail
        self.linkTail.prev = linknode

    def addFirst(self, linknode: LinkList):
        nex = self.linkHead.next
        self.linkHead.next = linknode
        linknode.prev = self.linkHead

        linknode.next = nex
        nex.prev = linknode

    def popLinkList(self, linknode: LinkList):
        prev = linknode.prev
        nex = linknode.next
        prev.next = nex
        nex.prev = prev
        linknode.prev = linknode.next = None

    def removeFrist(self):
        if self.linkHead.next == self.linkTail:
            pass

        else:
            nex = self.linkHead.next
            self.linkHead.next = nex.next
            nex.prev = self.linkHead
            nex.next = nex.prev = None

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.map:
            node = LinkNode(key, key)
            self.map[key] = node
            if node.count not in self.count_key:
                linklist = LinkList()
                # linklist.addFirst(node)
                self.addFirst(linklist)
                self.count_key[node.count] = linklist

            self.count_key[node.count].addFirst(node)

        else:
            node = self.map[key]
            self.count_key[node.count].popNode(node)
            if self.count_key[node.count].count == 0:
                self.popLinkList(self.count_key[node.count])
                del self.count_key[node.count]

            node.count += 1
            if node.count not in self.count_key:
                linklist = LinkList()
                self.addFirst(linklist)
                self.count_key[node.count] = linklist

            self.count_key[node.count].addFirst(node)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.map:
            node = self.map[key]
            self.count_key[node.count].popNode(node)
            if self.count_key[node.count].count == 0:
                self.popLinkList(self.count_key[node.count])
                del self.count_key[node.count]

            # 该元素则需要删除的操作!!!
            if node.count == 1:
                del self.map[key]
                return
            node.count -= 1

            if node.count not in self.count_key:
                linklist = LinkList()
                self.addLast(linklist)
                self.count_key[node.count] = linklist

            self.count_key[node.count].addFirst(node)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if len(self.count_key) == 0:
            return ''

        index = max(self.count_key.keys())
        return str(self.count_key[index].head.next.val)

        # linklist = self.linkTail.prev  # 可能指向tail节点
        # if linklist.count > 0:
        #     return str(linklist.head.next.val)
        # return ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """

        if len(self.count_key) == 0:
            return ''

        index = min(self.count_key.keys())
        return str(self.count_key[index].head.next.val)

        # linklist = self.linkHead.next  # 可能指向tail节点
        # if linklist.count > 0:
        #     return str(linklist.head.next.val)
        # return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

s = AllOne()
s.inc('hello')
s.inc('goodbye')
s.inc('hello')
s.inc('hello')
s.getMaxKey()
