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
        def rev_(n: Optional[ListNode]):
            if not n or not n.next: return n
            pre = n
            cur = n.next
            pre.next = None
            while cur:
                cur.next, cur, pre = pre, cur.next, cur
            return pre
        slow = fast = ListNode(0, head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        p2 = rev_(tmp)
        p1 = head
        while p1 and p2:
            if p1.val != p2.val: return False
            p1 = p1.next
            p2 = p2.next
        return True
# @lc code=end

