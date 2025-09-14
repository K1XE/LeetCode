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
        def rev(k):
            def rev_(node, k):
                pre = None
                cur = node.next
                for _ in range(k):
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                ret = node.next
                node.next.next = cur
                node.next = pre
                return ret

            dummy = ListNode(next=head)
            n = 0
            p = head
            while p:
                n += 1
                p = p.next
            p = dummy
            t = n // k
            for _ in range(t):
                p = rev_(p, k)
            return dummy.next

        return rev(k)


# @lc code=end
