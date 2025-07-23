#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = p1 = p2 = ListNode(next=head)
        while n:
            p2 = p2.next
            n -= 1
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next if p1.next else None
        return dummy.next
# @lc code=end

