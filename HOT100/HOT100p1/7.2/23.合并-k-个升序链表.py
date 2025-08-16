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
        h = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(h)
        prev = ListNode()
        curr = prev
        while h:
            _, i, node = heapq.heappop(h)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))

        return prev.next
# @lc code=end

