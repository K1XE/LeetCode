#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        def rev(pre, cur):
            pre_t = pre
            cur_t = cur
            while cur_t:
                tmp = cur_t.next
                cur_t.next = pre_t
                pre_t = cur_t
                cur_t = tmp
            pre.next = pre_t
            cur.next = cur_t
            return pre_t, cur
        pre = ListNode(next=head)
        return rev(pre, head)[0]
# @lc code=end

