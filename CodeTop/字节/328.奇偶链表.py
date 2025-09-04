#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        odd = ListNode(next=head)
        even = ListNode(next=head.next)
        p = head
        while p and p.next:
            ev = p.next
            p.next = ev.next
            p = ev
        p = odd.next
        while p.next: p = p.next
        p.next = even.next
        return odd.next
# @lc code=end

