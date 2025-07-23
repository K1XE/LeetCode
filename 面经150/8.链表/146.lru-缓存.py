#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
from collections import defaultdict
from typing import Optional
# @lc code=start
class Node:
    def __init__(self, k = 0, v = 0, nxt = None, pre = None):
        self.key = k
        self.val = v
        self.nxt = nxt
        self.pre = pre
class LRUCache:
    dummy = Node()
    def __init__(self, capacity: int):
        self.hash = defaultdict(Node)
        self.cnt = capacity
        self.dummy.nxt = self.dummy
        self.dummy.pre = self.dummy
    def rm_(self, n):
        n.pre.nxt = n.nxt
        n.nxt.pre = n.pre
    def push_front(self, n):
        self.dummy.nxt.pre = n
        n.nxt = self.dummy.nxt
        n.pre = self.dummy
        self.dummy.nxt = n
    def get_node(self, key):
        if key in self.hash:
            self.rm_(self.hash[key])
            self.push_front(self.hash[key])
            return self.hash[key]
        else: return None
    def get(self, key: int) -> int:
        tmp = self.get_node(key)
        if tmp: return tmp.val
        else: return -1

    def put(self, key: int, value: int) -> None:
        tmp = self.get_node(key)
        if tmp:
            tmp.val = value
        else:
            n = Node(key, value)
            self.push_front(n)
            self.hash[key] = n
            self.cnt -= 1
            if self.cnt < 0: 
                lxt = self.dummy.pre
                self.hash.pop(lxt.key)
                self.rm_(lxt)
                self.cnt = 0


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

