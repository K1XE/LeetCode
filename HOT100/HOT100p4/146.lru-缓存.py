#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
from mytools import *
# @lc code=start
class Node:
    def __init__(self, k=0, v=0, pre=None, nxt=None) -> None:
        self.k = k
        self.v = v
        self.pre = pre
        self.nxt = nxt
class LRUCache:

    def __init__(self, capacity: int):
        self.hash = defaultdict(Node)
        self.dummy = Node()
        self.dummy.pre = self.dummy
        self.dummy.nxt = self.dummy
        self.cnt = capacity
        
    def rm_(self, node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        return node
    
    def pf_(self, node):
        node.nxt = self.dummy.nxt
        self.dummy.nxt.pre = node
        node.pre = self.dummy
        self.dummy.nxt = node
        
    def get(self, key: int) -> int:
        if key in self.hash: 
            self.rm_(self.hash[key])
            self.pf_(self.hash[key])
            return self.hash[key].v
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash: self.hash[key].v = value; self.rm_(self.hash[key]); self.pf_(self.hash[key]); return
        self.cnt -= 1
        if self.cnt < 0:
            tmp = self.dummy.pre
            self.hash.pop(tmp.k)
            self.rm_(tmp)
            self.cnt += 1
        cur = Node(key, value)
        self.pf_(cur)
        self.hash[key] = cur
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

