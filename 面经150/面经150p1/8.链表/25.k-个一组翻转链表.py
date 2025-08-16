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
        dummy = cur = ListNode(next=head)
        def rev_(ppre: Optional[ListNode], p: Optional[ListNode]):
            cnt = k
            pre = None
            cur = p
            while cnt:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                cnt -= 1
            ppre.next.next = cur
            tmp = ppre.next
            ppre.next = pre
            return tmp, cur
        sz = 0
        p = head
        while p: sz += 1; p = p.next
        t = int(sz / k)
        p = head
        while t: cur, p = rev_(cur, p); t -= 1
        return dummy.next
# @lc code=end

