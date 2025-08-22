#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
from collections import defaultdict
# @lc code=start
class Node:
    def __init__(self, val = 0, key = 0, pre = None, next = None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre
class LRUCache:

    def __init__(self, capacity: int):
        self.c_ = capacity
        self.hash = defaultdict(Node)
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.pre = self.dummy
    def re_(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    def pf(self, node):
        node.next = self.dummy.next
        node.pre = self.dummy
        self.dummy.next.pre = node
        self.dummy.next = node
        p = self.dummy.next
    def get(self, key: int) -> int:
        if key in self.hash: self.re_(self.hash[key]); self.pf(self.hash[key]); return self.hash[key].val
        else: return -1
    def put(self, key: int, value: int) -> None:
        if key in self.hash: self.re_(self.hash[key]); self.pf(self.hash[key]); self.hash[key].val = value
        else:
            if self.c_ == 0: self.hash.pop(self.dummy.pre.key); self.re_(self.dummy.pre); self.c_ += 1
            self.c_ -= 1
            self.hash[key] = Node(val=value, key=key)
            self.pf(self.hash[key])

                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

