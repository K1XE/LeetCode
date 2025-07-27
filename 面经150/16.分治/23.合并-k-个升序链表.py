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
        for i in range(len(lists)):
            l = lists[i]
            if l: heapq.heappush(h, (l.val, i, l))
        dummy = cur = ListNode()
        while h:
            val, idx, node = heapq.heappop(h)
            cur.next = node
            cur = cur.next
            if node.next: heapq.heappush(h, (node.next.val, idx, node.next))
        return dummy.next
# @lc code=end

