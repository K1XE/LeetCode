#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
from typing import Optional
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False
# @lc code=end

