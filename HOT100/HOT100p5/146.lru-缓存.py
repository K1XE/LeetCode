#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
from mytools import *
# @lc code=start
class Node:
    def __init__(self, pre=None, nxt=None, val=-1, key=-1):
        self.pre = pre
        self.nxt = nxt
        self.val = val
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.dummy = Node()
        self.dummy.pre = self.dummy
        self.dummy.nxt = self.dummy
        self.c = capacity
        self.h = defaultdict(Node)

    def get(self, key: int) -> int:
        if key in self.h:
            tmp = self.h[key]
            tmp.pre.nxt = tmp.nxt
            tmp.nxt.pre = tmp.pre
            tmp.nxt = self.dummy.nxt
            self.dummy.nxt = tmp
            tmp.nxt.pre = tmp
            tmp.pre = self.dummy
            return self.h[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            cur = self.h[key]
            cur.val = value
            self.get(key)
            return
        if self.c == 0:
            tmp = self.dummy.pre
            tmp.pre.nxt = tmp.nxt
            tmp.nxt.pre = tmp.pre
            self.c += 1
            self.h.pop(tmp.key)
        self.c -= 1
        cur = Node(val=value, key=key)
        self.h[key] = cur
        cur.nxt = self.dummy.nxt
        cur.nxt.pre = cur
        self.dummy.nxt = cur
        cur.pre = self.dummy


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

