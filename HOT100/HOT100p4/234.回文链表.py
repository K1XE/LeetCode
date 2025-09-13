#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1 = l2 = ListNode(next=head)
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        h = l1
        pre = None
        cur = l1.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        h.next = pre
        l1 = head
        l2 = h.next
        while l2:
            if l1.val != l2.val: return False
            l1 = l1.next
            l2 = l2.next
        return True
# @lc code=end

