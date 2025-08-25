#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = ListNode(next=head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h = slow
        pre = None
        cur = h.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        h.next = pre
        p = head
        q = slow.next
        slow.next = None
        while p and q:
            tmp = q.next
            q.next = p.next
            p.next = q
            p = p.next.next
            q = tmp
        return head
# @lc code=end

