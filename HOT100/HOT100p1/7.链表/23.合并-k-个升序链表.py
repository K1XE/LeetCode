#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
from typing import Optional, List
import heapq
class ListNode:
    def __init__(self, _val, _next):
        self.val = _val
        self.next = _next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda a, b: a.val < b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        dummy = ListNode(0)
        cur = dummy
        h = [head for head in lists if head]
        heapq.heapify(h)
        while h:
            node = heapq.heappop(h)
            if node.next:
                heapq.heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next

# @lc code=end

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        dummy = ListNode(0)
        cur = dummy
        while self.check(lists):
            minVal = float('inf')
            minIdx = 0
            for i in range(k):
                if lists[i] and lists[i].val < minVal:
                    minVal = lists[i].val
                    minIdx = i
            cur.next = lists[minIdx]
            lists[minIdx] = lists[minIdx].next
            cur = cur.next
        return dummy.next
    def check(self, lists):
        for i in range(len(lists)):
            if lists[i] is not None:
                return True
        return False
            