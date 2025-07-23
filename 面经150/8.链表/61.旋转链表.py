#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        n = 0
        p = head
        while p: n += 1; p = p.next
        p = head
        k %= n
        if k == 0: return head
        dummy = ppre = ListNode(next=head)
        def rev(ppre: Optional[ListNode], p: Optional[ListNode], u):
            pre = None
            cur = p
            while u:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                u -= 1
            ppre.next.next = cur
            tmp = ppre.next
            ppre.next = pre
            return tmp, cur
        rev(ppre, p, n)
        ppre = dummy
        pre, cur = rev(ppre, ppre.next, k)
        rev(pre, cur, n - k)
        return dummy.next
# @lc code=end

