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
            while p: n += 1; p = p.next
            p = dummy
            t = n // k
            for _ in range(t):
                p = rev_(p, k)
            return dummy.next
        return rev(2)
        
# @lc code=end

