#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or a :
            if l1 :
                a += l1.val
                l1 = l1.next
            if l2 :
                a += l2.val
                l2 = l2.next
            cur.next = ListNode(a % 10)
            a = a // 10
            cur = cur.next
        return dummy.next
# @lc code=end

