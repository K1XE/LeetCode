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
        dummy = cur = ListNode()
        heapify(h)
        while h:
            _, i, node = heappop(h)
            cur.next = node
            cur = cur.next
            if node.next: heappush(h, (node.next.val, i, node.next))
        return dummy.next
        
# @lc code=end

