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
        dummy = ListNode(0, head)
        p1 = p2 = dummy
        for _ in range(n): p2 = p2.next
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return dummy.next
# @lc code=end

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2, dummy = ListNode(), ListNode(), ListNode()
        p1.next = head
        p2.next = head
        dummy.next = head
        while n:
            p2 = p2.next
            n -= 1
        f = True
        while p2.next:
            f = False
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return p1.next if f else dummy.next