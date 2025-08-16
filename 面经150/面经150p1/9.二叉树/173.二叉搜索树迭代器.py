#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#
from mytools import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        while root:
            self.stk.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stk.pop()
        node = cur.right
        while node:
            self.stk.append(node)
            node = node.left
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stk) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

