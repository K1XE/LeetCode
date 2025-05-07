#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from mytools import *
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(sta, res: List, pack: List):
            res.append(pack[:])
            for i in range(sta, n):
                pack.append(nums[i])
                dfs(i + 1, res, pack)
                pack.pop()
        res = []
        dfs(0, res, [])
        return res
# @lc code=end

