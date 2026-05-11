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
        h = []
        for i, l in enumerate(lists):
            if l: h.append((l.val, i, l))
        heapify(h)
        dummy = cur = ListNode()
        while h:
            val, idx, tmp = heappop(h)
            cur.next = tmp
            cur = cur.next
            if tmp.next: heappush(h, (tmp.next.val, idx, tmp.next))
        return dummy.next
            
                
# @lc code=end

