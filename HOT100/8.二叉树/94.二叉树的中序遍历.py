#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
from typing import Optional, List
class TreeNode:
    def __init__(self, _val = 0, left = None, right = None):
        self.val = _val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        res = []
        if root:
            stk.append((root, 0))
        while len(stk):
            node, visit = stk.pop()
            
            if visit:
                res.append(node.val)
                continue
            if node.right:
                stk.append((node.right, 0))
            stk.append((node, 1))
            if node.left:
                stk.append((node.left, 0))
        return res
# @lc code=end

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(n):
            if not n:
                return
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)
        dfs(root)
        return res