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
        res = []
        pack = []
        vis = [False] * n
        def dfs():
            if len(pack) == n: res.append(pack[:])
            for i in range(n):
                if vis[i]: continue
                vis[i] = True
                pack.append(nums[i])
                dfs()
                pack.pop()
                vis[i] = False
        dfs()
        return res
# @lc code=end

