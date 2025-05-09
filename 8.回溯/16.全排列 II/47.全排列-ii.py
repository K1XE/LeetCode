#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from mytools import *
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(vis, res: List, pack: List):
            if len(pack) == n:
                res.append(pack[:])
                return
            for i in range(n):
                if vis[i] == 1: continue
                if i > 0 and nums[i] == nums[i - 1] and vis[i - 1] == 0: continue
                pack.append(nums[i])
                vis[i] = 1
                dfs(vis, res, pack)
                vis[i] = 0
                pack.pop()
        res = []
        vis = [0] * n
        nums.sort()
        dfs(vis, res, [])
        return res
# @lc code=end

