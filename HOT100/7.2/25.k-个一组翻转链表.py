#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def re_(l: Optional[ListNode]):
            if not l or not l.next: return l, l
            prev = l
            cur = prev.next
            tail = prev
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev, tail
        if not head or not head.next: return head
        p = head
        rt = head
        f = True
        sz = 0
        while p:
            sz += 1
            p = p.next
        p = head
        preh, pret = ListNode(), ListNode()
        while sz // k:
            sta = p
            for _ in range(k - 1):
                p = p.next
            nxt = p.next
            p.next = None
            curh, curt = re_(sta)
            if f:
                rt = curh
                f = False
            if preh and pret:
                pret.next = curh
            p = nxt
            sz -= k
            preh, pret = curh, curt
        pret.next = p
        return rt
# @lc code=end

