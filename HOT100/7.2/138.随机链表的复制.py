#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

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
            cpy = Node(cur.val)
            cpy.next = cur.next
            cur.next = cpy
            cur = cpy.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head
        cpyhead = cur.next
        while cur:
            cpy = cur.next
            cur.next = cpy.next
            if cpy.next:
                cpy.next = cpy.next.next
            cur = cur.next
        return cpyhead
# @lc code=end

