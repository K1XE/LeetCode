#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from mytools import *
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        vis = [0] *  len(candidates)
        def dfs(sta, sums, res: List, pack: List):
            if sums == target:
                if pack not in res:
                    res.append(pack.copy())
                return
            for i in range(sta, len(candidates)):
                if i > sta and candidates[i - 1] == candidates[i] and vis[i - 1] == 0: continue
                sums += candidates[i]
                if sums > target:
                    sums -= candidates[i]
                    break
                pack.append(candidates[i])
                vis[i] = 1
                dfs(i + 1, sums, res, pack)
                sums -= candidates[i]
                vis[i] = 0
                pack.pop()
        res = []
        candidates.sort()
        dfs(0, 0, res, [])
        return res
# @lc code=end

