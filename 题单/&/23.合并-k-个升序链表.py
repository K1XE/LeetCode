#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapify(h)
        dummy = cur = ListNode()
        while h:
            val, idx, l = heappop(h)
            node = ListNode(val)
            cur.next = node
            cur = cur.next
            if l.next: heappush(h, (l.next.val, idx, l.next))
        return dummy.next
        
# @lc code=end

