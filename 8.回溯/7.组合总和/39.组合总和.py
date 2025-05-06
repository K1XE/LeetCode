#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
from mytools import *
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(sta, pack:List, res:List, sums):
            nonlocal target
            if sums == target:
                res.append(pack.copy())
                return
            for i in range(sta, len(candidates)):
                sums += candidates[i]
                if sums > target:
                    sums -= candidates[i]
                    break
                pack.append(candidates[i])
                dfs(i, pack, res, sums)
                pack.pop()
                sums -= candidates[i]
        res = []
        candidates.sort()
        dfs(0, [], res, 0)
        return res

# @lc code=end

