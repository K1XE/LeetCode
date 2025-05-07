#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 非递减子序列
#
from mytools import *
# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(sta, res: List, pack: List):
            if len(pack) >= 2:
                res.append(pack[:])
            seen = set()
            for i in range(sta, n):
                if pack and nums[i] < pack[-1]: continue                
                if nums[i] in seen: continue
                seen.add(nums[i])
                pack.append(nums[i])
                dfs(i + 1, res, pack)
                pack.pop()
        res = []
        dfs(0, res, [])
        return res
# @lc code=end

