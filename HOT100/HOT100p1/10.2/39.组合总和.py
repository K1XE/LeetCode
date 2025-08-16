#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from mytools import *
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res =[]
        pack = []
        sum_ = 0
        def dfs(sta, sum_):
            if sum_ == target:
                res.append(pack[:])
                return
            for i in range(sta, n):
                if sum_ + candidates[i] > target: break
                pack.append(candidates[i])
                dfs(i, sum_ + candidates[i])
                pack.pop()
        candidates.sort()
        dfs(0, 0)
        return res
# @lc code=end

