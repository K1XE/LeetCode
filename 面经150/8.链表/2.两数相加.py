#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        dummy = cur = ListNode()
        while l1 or l2 or s:
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            cur.next = ListNode(s % 10)
            s //= 10
            cur = cur.next
        return dummy.next
# @lc code=end

