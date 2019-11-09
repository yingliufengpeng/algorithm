# -*- coding: utf-8 -*-

from queue import PriorityQueue
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


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_node = {}
        self.node_key = {}
        self.count_nodelist = defaultdict(LinkList)
        self.k = 0

    def updateNode(self, node):
        c = node.count
        last_c = c - 1
        last_nodelist = self.count_nodelist[last_c]
        last_nodelist.popNode(node)
        new_nodelist = self.count_nodelist[c]
        new_nodelist.addFirst(node)

    def get(self, key: int) -> int:
        if key in self.key_node:
            node = self.key_node[key]
            node.count += 1
            self.updateNode(node)
            # print('get', node.val)
            return node.val

        else:
            return -1

    def addNewNode(self, key, val):
        node = LinkNode(key, val)
        self.key_node[key] = node
        self.node_key[node] = key
        c = node.count
        new_nodelist = self.count_nodelist[c]
        new_nodelist.addFirst(node)
        self.k += 1

    def deleteNode(self):
        for k in self.count_nodelist:
            # print('k is', k)
            nodelist = self.count_nodelist[k]
            if nodelist.count > 0:
                node = nodelist.tail.prev
                kv = self.node_key[node]
                del self.node_key[node]
                del self.key_node[kv]
                nodelist.removeLast()
                break
        self.k -= 1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.key_node:
            # if self.cap
            if self.k == self.cap:
                self.deleteNode()

            self.addNewNode(key, value)
        else:
            node = self.key_node[key]
            node.val = value
            node.count += 1
            self.updateNode(node)


class LFUCache2:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map: 'int -> LinkNode' = {}
        self.map2: 'LinkNode -> int' = {}
        self.head = LinkNode(None, None)
        self.tail = LinkNode(None, None)

        # self.p = PriorityQueue() # 优先队列,升序排序
        self.map3: 'count -> set(LinkNode)' = defaultdict(set)  # 根据访问次数快速查找

        self.link(self.head, self.tail)
        # self.link(self.tail, self.head)   # 不是循环链表

    # 注意count已经加过
    def updateCount(self, node):
        #
        c = node.count
        # print('update', node)
        if c == 1:
            self.map3[c] |= {node}
        else:

            self.map3[c] |= {node}
            self.map3[c - 1] -= {node}

        # self.p.put(c)

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]

            node.count += 1
            v = node.val

            self.updateCount(node)

            self.moveToFristNode(node)
            return v
        else:
            return -1

    # from node2 to node2
    def link(self, node1, node2):
        node1.next = node2
        node2.prev = node1

    def put(self, key: int, value: int) -> None:

        if self.cap <= 0:
            return

            # print('self.map ', len(self.map))
        # print('len(self.map) == self.cap  self.cap', len(self.map) == self.cap, self.cap)
        if key not in self.map:
            if len(self.map) == self.cap:
                # print('mapddddd 10')
                self.deleteLastnode()
            node = LinkNode(key, value)
            t = self.head.next
            self.link(self.head, node)
            self.link(node, t)
            self.map[key] = node
            self.map2[node] = key

            self.updateCount(node)
        else:
            node = self.map[key]
            node.val = value
            node.count += 1

            self.updateCount(node)
            # self.map2[node] = value
            self.moveToFristNode(node)

    def moveToFristNode(self, node):
        prev = node.prev
        nex = node.next
        self.link(prev, nex)
        t = self.head.next
        self.link(self.head, node)
        self.link(node, t)

    def deleteLastnode(self):

        node = None
        keys = sorted(self.map3.keys())
        for k in keys:
            if self.map3[k]:
                # print('map3', self.map3)
                if len(self.map3[k]) == 1:
                    node = self.map3[k].pop()
                    # print('node is', node)
                else:
                    pass
                break
        if node is None:
            node = self.tail.prev
        # node = self.tail.prev
        if node == self.head:
            pass
        else:
            # print('map2', self.map2)
            k = self.map2[node]
            prev = node.prev
            node.next = node.prev = None
            self.link(prev, self.tail)

            # map3中也许会有数据
            del self.map[k]
            del self.map2[node]
            for k in self.map3:
                if node in self.map3[k]:
                    self.map3[k] -= {node}
                    break


L = ["LFUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
L = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]

R = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

R = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
t = list(zip(L, R))
A, p = t[0]

o = globals()[A](*p)
res = [None]
for method, p in t[1:]:
    r = getattr(o, method)(*p)
    res.append(r)

print(res)
