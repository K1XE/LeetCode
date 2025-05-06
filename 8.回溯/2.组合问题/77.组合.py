#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from mytools import *
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(sta, pack: List):
            if len(pack) == k:
                nonlocal res
                res.append(pack[:])
                return
            for i in range(sta, n - (k - len(pack)) + 2):
                pack.append(i)
                dfs(i + 1, pack)
                pack.pop()
            return
        dfs(1, [])
        return res
# @lc code=end

