#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next=head)
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast and slow != None: return True
        return False
# @lc code=end

