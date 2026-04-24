#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from mytools import *
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        vis = [False] * n
        res = []
        pack = []
        def dfs(sta):
            nonlocal n
            res.append(pack[:])
            for i in range(sta, n):
                if vis[i]: continue
                vis[i] = True
                pack.append(nums[i])
                dfs(i + 1)
                pack.pop()
                vis[i] = False
        dfs(0)
        return res
                
# @lc code=end

