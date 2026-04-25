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
        cur = 0
        
        dummy = ListNode()
        res = dummy
        while l1 or l2 or cur:
            if l1: cur += l1.val; l1 = l1.next
            if l2: cur += l2.val; l2 = l2.next
            tmp = ListNode(val=cur % 10)
            cur //= 10
            res.next = tmp
            res = res.next
        return dummy.next
            
# @lc code=end

