#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#
from mytools import *
class Node:
    def __init__(self, x = 0, random = None, next = None) -> None:
        self.val = x
        self.random = random
        self.next = next
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
        p = head
        while p:
            tmp = Node(x=p.val, next=p.next)
            p.next = tmp
            p = tmp.next
        p = head
        while p:
            if p.random: p.next.random = p.random.next
            p = p.next.next
        p = head
        dummy = cur = Node(0)
        while p:
            cur.next = p.next
            cur = cur.next
            p.next = p.next.next
            p = p.next
        return dummy.next
# @lc code=end

