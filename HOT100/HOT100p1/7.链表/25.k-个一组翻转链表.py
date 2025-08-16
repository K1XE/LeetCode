#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
from typing import Optional
class ListNode :
    def __init__(self, val, next):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, pre, starts, ends) :
        u = pre.next
        pre.next = ends
        while starts != ends :
            tmp = starts.next
            starts.next = pre.next
            pre.next = starts
            starts = tmp
        pre = u
        return pre, starts, ends
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        back = k
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        starts = head
        ends = starts
        while ends :
            k -= 1
            ends = ends.next
            if not k :
                pre, ends, starts = self.reverseList(pre, starts, ends)
                k += back
        return dummy.next
# @lc code=end

