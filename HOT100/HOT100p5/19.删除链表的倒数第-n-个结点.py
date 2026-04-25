#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next: return None
        dummy = ListNode(next=head)
        tmp = dummy
        cur = dummy
        for _ in range(n):
            tmp = tmp.next
        while tmp.next:
            cur = cur.next
            tmp = tmp.next
        cur.next = cur.next.next if cur.next else None
        return dummy.next
# @lc code=end

