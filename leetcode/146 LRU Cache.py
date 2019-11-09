# -*- coding: utf-8 -*-
from queue import PriorityQueue
from collections import defaultdict
class LinkNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

    def __str__(self):
        return '{} {}'.format(self.key, self.val)

    __repr__ = __str__


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map: 'int -> LinkNode' = {}
        self.map2: 'LinkNode -> int' = {}
        self.head = LinkNode(None, None)
        self.tail = LinkNode(None, None)

        self.link(self.head, self.tail)
        # self.link(self.tail, self.head)   # 不是循环链表

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            v = node.val
            self.moveToFristNode(node)
            return v
        else:
            return -1

    # from node2 to node2
    def link(self, node1, node2):
        node1.next = node2
        node2.prev = node1

    def put(self, key: int, value: int) -> None:
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
        else:
            node = self.map[key]
            node.val = value
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
        node = self.tail.prev
        if node == self.head:
            pass
        else:
            k = self.map2[node]
            prev = node.prev
            node.next = node.prev = None
            self.link(prev, self.tail)
            del self.map[k]
            del self.map2[node]


# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)
# cache.put(3, 3)
# cache.get(2)
# cache.put(4, 4)
# cache.get(1)
# cache.get(3)
# cache.get(4)
# cache.get(2)
# cache.put(2, 6)
# cache.get(1)
# cache.put(1, 5)
# cache.put(1, 2)
# cache.get(1)
# cache.get(2)
# cache.put(2, 5)
# cache.get(1)
# cache.get(3)
# cache.get(2)

L = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
     "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
     "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
     "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
     "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
     "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
     "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]

# L = ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
R = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
     [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11], [8],
     [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9],
     [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22], [11, 26], [8, 17],
     [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20],
     [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19],
     [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
     [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
# R = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]

t = list(zip(L, R))
A, p = t[0]

o = globals()[A](*p)
res = [None]
for method, p in t[1:]:
    r = getattr(o, method)(*p)
    res.append(r)
print('cap', o.cap)
print('size of map', len(o.map))

print('size of map2', len(o.map2))

i = 0
cur = o.head

while cur:
    i += 1
    cur = cur.next

print(i - 2)
print(res)