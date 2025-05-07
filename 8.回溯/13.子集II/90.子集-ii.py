#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
from mytools import *
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        def dfs(vis: List, res: List, pack: List, sta):
            res.append(pack.copy())
            for i in range(sta, n):
                if i > sta and nums[i] == nums[i - 1] and vis[i] == 0:
                    continue
                vis[i] = 1
                pack.append(nums[i])
                dfs(vis, res, pack, i + 1)
                pack.pop()
                vis[i] = 0

        res = []
        vis = [0] * n
        nums.sort()
        dfs(vis, res, [], 0)
        return res
                
# @lc code=end

