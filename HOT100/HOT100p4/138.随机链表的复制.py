#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#
from mytools import *
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        while cur:
            p = Node(x=cur.val, next=cur.next)
            cur.next = p
            cur = p.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        dummy = res = Node(1)
        cur = head
        while cur:
            res.next = cur.next
            res = res.next
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next
            
# @lc code=end

