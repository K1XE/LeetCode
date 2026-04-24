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
        def rev_(pre, n, k):
            cur = n
            tmp = None
            h = pre
            pre.next = None
            while k:
                tmp = cur.next
                cur.next = pre
                pre = cur 
                cur = tmp
                k -= 1
            n.next = cur
            h.next = pre
            return pre, n
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        t = cnt // k
        cur = head
        pre = ListNode(next=cur)
        f = False
        ret = head
        print(t)
        while t:
            t -= 1
            h_, t_ = rev_(pre, cur, k)
            if not f:
                f = True
                ret = h_
            pre = t_
            cur = t_.next
        return ret
                
            
# @lc code=end

