#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
from mytools import *
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(n, k, sta, pack: List, sums):
            if len(pack) == k:
                if sums == n:
                    nonlocal res
                    res.append(pack.copy())
                return
            for i in range (sta, 9 - (k - len(pack)) + 2):
                sums += i
                if sums > n:
                    sums -= i
                    break
                pack.append(i)
                dfs(n, k, i + 1, pack, sums)
                sums -= i
                pack.pop()
            return
        dfs(n, k, 1, [], 0)
        return res

# @lc code=end

