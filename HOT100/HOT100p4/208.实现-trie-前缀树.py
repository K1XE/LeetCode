#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
from mytools import *
# @lc code=start
class Node:
    def __init__(self, end=False) -> None:
        self.son = [None] * 26
        self.end = end
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if cur.son[idx] is None: cur.son[idx] = Node()
            cur = cur.son[idx]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if cur.son[idx] is None: return False
            cur = cur.son[idx]
        return cur.end
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if cur.son[idx] is None: return False
            cur = cur.son[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

