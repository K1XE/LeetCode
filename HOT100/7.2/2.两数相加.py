#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or x:
            if l1:
                x += l1.val
                l1 = l1.next
            if l2:
                x += l2.val
                l2 = l2.next
            cur.next = ListNode(x % 10)
            cur = cur.next
            x //= 10
        return dummy.next
# @lc code=end

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1, x2 = 0, 0
        t = 0
        p1, p2 = l1, l2
        while p1:
            x1 += p1.val * 10 ** t
            t += 1
            p1 = p1.next
        t = 0
        while p2:
            x2 += p2.val * 10 ** t
            t += 1
            p2 = p2.next
        x = x1 + x2
        if x == 0: return ListNode(0)
        cur = ListNode()
        dummy = ListNode(0, cur)
        while x:
            tmp = x % 10
            x //= 10
            print(tmp, x)
            u = ListNode(tmp)
            cur.next = u
            cur = cur.next
        return dummy.next.next
