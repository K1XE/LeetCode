#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class Node:
    def __init__(self, _key, _val):
        self.key = _key
        self.val = _val
        self.next = None
        self. prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self._c = capacity
        self.dummy = Node(0, 0)
        self.hash = dict()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def remove(self, n):
        n.next.prev = n.prev
        n.prev.next = n.next

    def push_front(self, n):
        n.next = self.dummy.next
        n.prev = self.dummy
        self.dummy.next.prev = n
        self.dummy.next = n

    def get_node(self, key):
        if key not in self.hash:
            return None
        node = self.hash[key]
        self.remove(node)
        self.push_front(node)
        return node
    
    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = value
            self.remove(node)
            self.push_front(node)
            return
        tmp = Node(key, value)
        self.push_front(tmp)
        self.hash[key] = tmp
        if len(self.hash) > self._c:
            u = self.dummy.prev
            self.remove(u)
            del self.hash[u.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

