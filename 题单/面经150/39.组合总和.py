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
        res = []
        pack = []
        s = 0
        def dfs(sta):
            nonlocal s
            if s == target: res.append(pack[:]); return
            for i in range(sta, n):
                if s + candidates[i] > target: break
                s += candidates[i]
                pack.append(candidates[i])
                dfs(i)
                pack.pop()
                s -= candidates[i]
        candidates.sort()
        dfs(0)
        return res
# @lc code=end

