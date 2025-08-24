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
        if k == 1: return head
        def re_(n):
            ret = n.next
            pre = None
            cur = n.next
            for _ in range(k):
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            n.next.next = cur
            n.next = pre
            return ret
        cnt = 0
        p = head
        while p: cnt += 1; p = p.next
        t = cnt // k
        dummy = cur = ListNode(next=head)
        while t:
            cur = re_(cur)
            t -= 1
        return dummy.next
# @lc code=end

