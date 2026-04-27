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
        cnt = 0
        dummy = cur = ListNode()
        while cnt or l1 or l2:
            if l1: cnt += l1.val; l1 = l1.next
            if l2: cnt += l2.val; l2 = l2.next
            cur.next = ListNode(val=cnt % 10)
            cur = cur.next
            cnt //= 10
        return dummy.next
# @lc code=end

