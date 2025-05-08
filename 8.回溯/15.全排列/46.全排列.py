#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from mytools import *
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(vis: List, res: List, pack: List):
            if len(pack) == n:
                res.append(pack.copy())
                return
            
            for i in range(0, n):
                if vis[i] == 1: continue
                vis[i] = 1
                pack.append(nums[i])
                dfs(vis, res, pack)
                pack.pop()
                vis[i] = 0
            
        res = []
        vis = [0] * n
        dfs(vis, res, [])
        return res

# @lc code=end

