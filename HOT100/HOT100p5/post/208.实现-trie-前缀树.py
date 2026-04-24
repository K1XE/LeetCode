#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
from mytools import *
# @lc code=start
class Node:
    def __init__(self, end=False):
        self.child = defaultdict(Node)
        self.end = end
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node()
            cur = cur.child[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.child: return False
            cur = cur.child[ch]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.child: return False
            cur = cur.child[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

