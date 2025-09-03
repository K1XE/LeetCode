#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode(next=head)
        p = head
        while p and p.next:
            if p.next.val == p.val:
                val = p.val
                nxt = p.next
                while nxt and nxt.val == val: nxt = nxt.next
                p.next = nxt
            p = p.next

        return dummy.next
# @lc code=end

