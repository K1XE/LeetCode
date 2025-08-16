#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
from collections import defaultdict
# @lc code=start
class Node:
    def __init__(self, end = False):
        self.end = end
        self.son = defaultdict(Node)
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word: cur = cur.son[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        return self.match(word, 0, self.root)

    def match(self, word, idx, cur):
        if cur == None: return False
        if len(word) == idx: return cur.end
        if word[idx] != '.':
            return cur != None and self.match(word, idx + 1, cur.son.get(word[idx]))
        else:
            for child in cur.son.values():
                if self.match(word, idx + 1, child): return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

