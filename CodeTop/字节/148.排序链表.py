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
        pre = None
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        l1 = head; l2 = slow
        pre.next = None
        h1 = self.sortList(l1); h2 = self.sortList(l2)
        return self.merge(h1, h2)
    def merge(self, h1, h2):
        dummy = cur = ListNode()
        while h1 and h2:
            if h1.val > h2.val: cur.next = h2; h2 = h2.next
            else: cur.next = h1; h1 = h1.next
            cur = cur.next
        cur.next = h1 if h1 else h2
        return dummy.next
        
# @lc code=end

