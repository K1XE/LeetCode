#
# @lc app=leetcode.cn id=3217 lang=python3
#
# [3217] 从链表中移除在数组中存在的节点
#
from mytools import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        hash = set(nums)
        pre = dummy
        p = head
        while p:
            if p.val in hash:
                pre.next = p.next
                p = pre.next
            else:
                pre = p
                p = p.next
        return dummy.next
# @lc code=end

