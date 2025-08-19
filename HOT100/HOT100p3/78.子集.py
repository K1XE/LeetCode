#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from mytools import *
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(sta, pack):
            res.append(pack[:])
            for i in range(sta, n):
                pack.append(nums[i])
                dfs(i + 1, pack)
                pack.pop()
        dfs(0, [])
        return res
# @lc code=end

