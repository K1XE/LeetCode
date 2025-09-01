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
        res = []
        vis = [False] * n
        nums.sort()
        def dfs(pack):
            if len(pack) == n: res.append(pack[:]); return
            for i in range(n):
                if vis[i] or (i > 0 and nums[i] == nums[i - 1] and not vis[i - 1]): continue
                vis[i] = True
                pack.append(nums[i])
                dfs(pack)
                pack.pop()
                vis[i] = False
        dfs([])
        return res
# @lc code=end

