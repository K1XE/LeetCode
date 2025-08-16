#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
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
        l1 = head; l2 = pre.next
        pre.next = None
        n1 = self.sortList(l1); n2 = self.sortList(l2)
        return self.merge(n1, n2)
    def merge(self, l1, l2):
        cur = dummy = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next
# @lc code=end

