#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            else:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        return dummy.next
# @lc code=end

