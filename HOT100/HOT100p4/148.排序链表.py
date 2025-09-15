#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        slow = fast = ListNode(next=head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h1 = head; h2 = slow.next
        slow.next = None
        l1 = self.sortList(h1); l2 = self.sortList(h2)
        return self.merge_(l1, l2)
    def merge_(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val > l2.val: cur.next = l2; l2 = l2.next
            else: cur.next = l1; l1 = l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

        
# @lc code=end

