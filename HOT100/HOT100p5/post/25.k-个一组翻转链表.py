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
        def rev(pre, cur, k):
            pre_t = None
            cur_t = cur
            for _ in range(k):
                tmp = cur_t.next
                cur_t.next = pre_t
                pre_t = cur_t
                cur_t = tmp
            cur.next = cur_t
            pre.next = pre_t
            return pre_t, cur
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next
        t = cnt // k
        cur = head
        pre = ListNode(next=cur)
        f = False
        res = head
        for _ in range(t):
            h_, t_ = rev(pre, cur, k)
            if not f: res = h_; f = True
            pre = t_; cur = t_.next
        return res
# @lc code=end

