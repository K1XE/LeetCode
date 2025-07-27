#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from typing import List
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        pack = []
        def dfs(sta):
            if len(pack) == k:
                res.append(pack[:])
                return
            for i in range(sta, n + 1):
                pack.append(i)
                dfs(i + 1)
                pack.pop()
        dfs(1)
        return res
# @lc code=end

