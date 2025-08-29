#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from mytools import *
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def dfs(sta, pack, s):
            if s == target:
                res.append(pack[:])
                return
            for i in range(sta, n):
                if i > sta and candidates[i] == candidates[i - 1]: continue
                if s + candidates[i] > target: break
                s += candidates[i]
                pack.append(candidates[i])
                dfs(i + 1, pack, s)
                pack.pop()
                s -= candidates[i]
        candidates.sort()
        print(candidates)
        dfs(0, [], 0)
        return res
# @lc code=end

