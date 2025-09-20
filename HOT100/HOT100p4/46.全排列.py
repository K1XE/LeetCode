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
            nonlocal n
            if len(pack) == n:
                res.append(pack[:])
                return
            for i in range(n):
                if vis[i] == True: continue
                pack.append(nums[i])
                vis[i] = True
                dfs()
                pack.pop()
                vis[i] = False
        dfs()
        return res
# @lc code=end

