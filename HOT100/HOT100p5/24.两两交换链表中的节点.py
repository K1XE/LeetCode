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
        def rev_(pre, cur, k):
            pre_t = None
            cur_t = cur
            for _ in range(k):
                tmp = cur_t.next
                cur_t.next = pre_t
                pre_t = cur_t
                cur_t = tmp
            pre.next = pre_t
            cur.next = cur_t
            return pre, cur
        cnt = 0
        n = head
        while n:
            cnt += 1
            n = n.next
        if cnt <= 1: return head
        t = cnt // 2
        pre = ListNode(next=head)
        cur = head
        f = False
        res = head
        for _ in range(t):
            h_, t_ = rev_(pre, cur, 2)
            if not f: res = h_; f = True
            pre = t_
            cur = t_.next
        return res.next
# @lc code=end

