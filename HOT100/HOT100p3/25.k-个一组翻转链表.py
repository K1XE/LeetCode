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
        if k <= 1: return head
        def re_(l, k):
            lxt = l.next
            pre = l.next
            cur = pre.next
            pre.next = None
            for _ in range(k - 1):
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            l.next = pre
            lxt.next = cur
            print(l.next.val)
            return lxt
        cnt = 0
        p = head
        while p:
            cnt += 1
            p = p.next
        t = cnt // k
        nxt = ListNode(next=head)
        dummy = ListNode(next=nxt)
        for _ in range(t):
            nxt = re_(nxt, k)
        return dummy.next.next
# @lc code=end

