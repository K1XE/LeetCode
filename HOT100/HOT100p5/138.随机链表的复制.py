#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#
from mytools import *
class Node:
    def __init__(self, x, next=None, random=None):
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
        dummy = cur = Node(x=-1, next=head)
        cur = cur.next
        while cur:
            tmp = Node(x=cur.val, next=cur.next)
            nxt = cur.next
            cur.next = tmp
            cur = nxt
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        ret = head.next
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next
            cur = cur.next
        return ret
# @lc code=end

