#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
from mytools import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        hash = defaultdict(int)
        hash[0] = 1
        def dfs(n, val):
            if not n: return
            val += n.val
            nonlocal cnt
            cnt += hash[val - targetSum]
            hash[val] += 1
            dfs(n.left, val)
            dfs(n.right, val)
            hash[val] -= 1
        dfs(root, 0)
        return cnt
# @lc code=end

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        def dfs(n, sums):
            if not n : return
            nonlocal cnt
            if sums == targetSum: cnt += 1
            if n.left:
                sums += n.left.val
                dfs(n.left, sums)
                sums -= n.left.val
            if n.right:
                sums += n.right.val
                dfs(n.right, sums)
                sums -= n.right.val
            return
            
        if not root: return 0
        q = deque()
        q.append(root)
        while q:
            tmp = q.popleft()
            dfs(tmp, tmp.val)
            if tmp.left: q.append(tmp.left)
            if tmp.right: q.append(tmp.right)
        
        return cnt