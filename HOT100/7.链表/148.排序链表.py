#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
from typing import Optional
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self, n):
        len = 0
        while (n):
            len += 1
            n = n.next
        return len
    def split(self, n, i):
        if not n: return None
        cur = n
        for _ in range(0, i - 1):
            if cur is None:
                break
            cur = cur.next

        if not cur or not cur.next: return None
        next_head = cur.next
        cur.next = None
        return next_head
    def merge(self, h1, h2):
        cur = dummy = ListNode(0)
        while h1 and h2:
            if h1.val > h2.val:
                cur.next = h2
                h2 = h2.next
            else:
                cur.next = h1
                h1 = h1.next
            cur = cur.next
        cur.next = h1 if h1 else h2
        while cur.next:
            cur = cur.next
        return [dummy.next, cur]
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.get_len(head)
        dummy = ListNode(0)
        dummy.next = head
        i = 1
        while i < l:
            new_list_tail = dummy
            cur = dummy.next
            while cur:
                head1 = cur
                head2 = self.split(head1, i)
                cur = self.split(head2, i)
                [head, tail] = self.merge(head1, head2)
                new_list_tail.next = head
                new_list_tail = tail
            i *= 2
        return dummy.next


# @lc code=end

