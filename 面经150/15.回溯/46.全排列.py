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
        pack = []
        n = len(nums)
        vis = set()
        def dfs():
            if len(pack) == n:
                res.append(pack[:])
                return
            for i in range(n):
                if nums[i] in vis: continue
                pack.append(nums[i])
                vis.add(nums[i])
                dfs()
                pack.pop()
                vis.remove(nums[i])
        dfs()
        return res
# @lc code=end

