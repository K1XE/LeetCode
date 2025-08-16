#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev_(l: Optional[ListNode]):
            if not l or not l.next: return l, l
            prev, cur = l, l.next
            dummy = l
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev, dummy
        if not head or not head.next: return head
        dummy = ListNode(next=head.next)
        sz = 0
        p = head
        while p:
            sz += 1
            p = p.next
        preh, pret = None, None
        p = head
        while sz // 2:
            sta = p
            p = p.next
            nxt = p.next
            p.next = None
            curh, curt = rev_(sta)
            if pret:
                pret.next = curh
            sz -= 2
            p = nxt
            preh, pret = curh, curt
        pret.next = p
        return dummy.next
# @lc code=end

