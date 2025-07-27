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
        res = []
        pack = []
        n = len(candidates)
        def dfs(s, sta):
            if s == target:
                res.append(pack[:])
                return
            for i in range(sta, n):
                s += candidates[i]
                if s > target:
                    s -= candidates[i]
                    break
                pack.append(candidates[i])
                dfs(s, i)
                pack.pop()
                s -= candidates[i]
        dfs(0, 0)
        return res
# @lc code=end

