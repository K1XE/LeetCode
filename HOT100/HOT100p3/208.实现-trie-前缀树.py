#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Node:
    def __init__(self) -> None:
        self.child = [None] * 26
        self.end = False
class Trie:
    
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if cur.child[idx] is None: cur.child[idx] = Node()
            cur = cur.child[idx]
        cur.end = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if cur.child[idx] is None: return False
            cur = cur.child[idx]
        return cur.end
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if cur.child[idx] is None: return False
            cur = cur.child[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

