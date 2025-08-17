#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        pack = []
        def dfs(sta, s):
            if s == target:
                res.append(pack[:])
                return
            for i in range(sta, n):
                if s + candidates[i] > target: break
                s += candidates[i]
                pack.append(candidates[i])
                dfs(i, s)
                pack.pop()
                s -= candidates[i]
        dfs(0, 0)
        return res
# @lc code=end

