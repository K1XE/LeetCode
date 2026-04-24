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
            
        l1, l2 = head, slow.next
        slow.next = None
        h1, h2 = self.sortList(l1), self.sortList(l2)
        return self.m_(h1, h2)
    def m_(self, n1, n2):
        dummy = cur = ListNode()
        while n1 and n2:
            if n1.val > n2.val: cur.next = n2; n2 = n2.next; cur = cur.next
            else: cur.next = n1; n1 = n1.next; cur = cur.next
        cur.next = n1 if n1 else n2
        return dummy.next
            
# @lc code=end

