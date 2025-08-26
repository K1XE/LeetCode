#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None) -> None:
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
        while fast:
            slow = slow.next
            if not fast.next: return False
            fast = fast.next.next
            if slow == fast: return True
        
# @lc code=end

