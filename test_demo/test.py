# -*- coding: utf-8 -*-

from collections import OrderedDict
class Trie:
    n = 26

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.children = {}

        self.is_end = False

    def show(self) -> str:

        res = ['']

        ks = self.children.keys()

        ks = sorted(ks)

        for k in ks:
            res.append(k)

            r = self.children[k].show()

            res.append(r)

        return ''.join(res)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        """

        if not word:
            self.is_end = True

            return None

        c = word[0]

        if c not in self.children:

            n = self.children[c] = Trie()

        else:

            n = self.children[c]

        n.insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        if not word:
            return self.is_end

        c = word[0]

        if c in self.children:

            return self.children[c].search(word[1:])

        else:

            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True

        c = prefix[0]
        # print('c', c)

        if c in self.children:

            return self.children[c].startsWith(prefix[1:])

        else:

            return False


# Your Trie object will be instantiated and called as such:
trie = Trie()

trie.insert("yingliufengpeng")

r = trie.search("apple")  # 返回 true
r2 = trie.search("app")  # 返回 false
r3 = trie.startsWith("app")  # 返回 true
trie.insert("app")
trie.search("app")  # 返回 true


ans = trie.show()

print(ans)
