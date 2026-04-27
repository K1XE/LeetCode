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
        if not head or not head.next: return True
        slow = fast = ListNode(next=head)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        def rev(pre, cur):
            pre_t = None
            cur_t = cur
            while cur_t:
                tmp = cur_t.next
                cur_t.next = pre_t
                pre_t = cur_t
                cur_t = tmp
            pre.next = pre_t
            cur.next = cur_t
            return pre_t, cur
        rev(slow, slow.next)
        h1 = head; h2 = slow.next
        while h1 and h2:
            if h1.val != h2.val: return False
            h1 = h1.next
            h2 = h2.next
        return True
# @lc code=end

