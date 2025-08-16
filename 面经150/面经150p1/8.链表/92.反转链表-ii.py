#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = dummy = ListNode(0, head)
        
        l = left - 1
        r = right - 1
        d = r - l + 1
        while l:
            cur = cur.next
            l -= 1
        p = cur.next
        pre = None
        while d:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
            d -= 1
        cur.next.next = p
        cur.next = pre
        return dummy.next
# @lc code=end

