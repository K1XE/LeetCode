#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
        cur = dummy = ListNode(next=head)

        while cur.next and cur.next.next:
            val = cur.next.val
            if val == cur.next.next.val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else: cur = cur.next
        return dummy.next
# @lc code=end

