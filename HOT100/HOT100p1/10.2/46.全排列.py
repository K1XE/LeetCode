#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from mytools import *
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        vis = [False] * n
        def dfs(pack: List):
            if len(pack) == n:
                res.append(pack[:])
                return
            for i in range(n):
                if vis[i]: continue
                pack.append(nums[i])
                vis[i] = True
                dfs(pack)
                vis[i] = False
                pack.pop()
        dfs([])
        return res
# @lc code=end

