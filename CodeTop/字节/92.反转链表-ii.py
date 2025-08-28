#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        cnt = 0
        while pre and pre.next:
            cnt += 1
            if cnt == left:
                u = pre
                cur = pre.next
                pre = None
                while cnt <= right:
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                    cnt += 1
                u.next.next = cur
                u.next = pre
                break
            pre = pre.next
            
        return dummy.next

# @lc code=end

