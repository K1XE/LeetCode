#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
from mytools import *
# @lc code=start
class Node:
    def __init__(self, pre=None, nxt=None, key=-1, val=-1):
        self.pre = pre
        self.nxt = nxt
        self.key = key
        self.val = val
class LRUCache:

    def __init__(self, capacity: int):
        self.dummy = Node()
        self.dummy.pre = self.dummy
        self.dummy.nxt = self.dummy
        self.h = defaultdict(Node)
        self.c = capacity
    def rm(self, n):
        n.nxt.pre = n.pre
        n.pre.nxt = n.nxt
    def pf(self, n):
        n.nxt = self.dummy.nxt
        n.pre = self.dummy
        self.dummy.nxt = n
        n.nxt.pre = n

    def get(self, key: int) -> int:
        if key in self.h:
            self.rm(self.h[key])
            self.pf(self.h[key])
            return self.h[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.h:
            self.rm(self.h[key])
            self.pf(self.h[key])
            self.h[key].val = value
        else:
            if self.c == 0:
                self.h.pop(self.dummy.pre.key)
                self.rm(self.dummy.pre)
                self.c += 1
            self.c -= 1
            self.h[key] = Node(key=key, val=value)
            self.pf(self.h[key])
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

