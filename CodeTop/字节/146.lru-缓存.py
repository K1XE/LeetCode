#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
from mytools import *


# @lc code=start
class Node:
    def __init__(self, key=0, val=0, nxt=None, pre=None) -> None:
        self.key = key
        self.val = val
        self.nxt = nxt
        self.pre = pre


class LRUCache:
    def __init__(self, capacity: int):
        self.c_ = capacity
        self.dummy = Node()
        self.dummy.nxt = self.dummy
        self.dummy.pre = self.dummy
        self.hash = defaultdict(Node)

    def re_(self, node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre

    def pf(self, node):
        node.nxt = self.dummy.nxt
        node.pre = self.dummy
        self.dummy.nxt = node
        node.nxt.pre = node

    def get(self, key: int) -> int:
        if key in self.hash:
            self.re_(self.hash[key])
            self.pf(self.hash[key])
            return self.hash[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key].val = value
            self.re_(self.hash[key])
            self.pf(self.hash[key])
        else:
            if self.c_ == 0:
                self.hash.pop(self.dummy.pre.key)
                self.re_(self.dummy.pre)
                self.c_ += 1
            self.c_ -= 1
            self.hash[key] = Node(key, value)
            self.pf(self.hash[key])
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
