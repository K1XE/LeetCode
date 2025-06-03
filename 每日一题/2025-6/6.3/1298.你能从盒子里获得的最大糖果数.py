#
# @lc app=leetcode.cn id=1298 lang=python3
#
# [1298] 你能从盒子里获得的最大糖果数
#
from mytools import *
# @lc code=start
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        has_key = status
        n = len(status)
        has_box = [False] * n
        for idx in initialBoxes:
            has_box[idx] = True
        res = 0
        def dfs(x):
            nonlocal res
            res += candies[x]
            has_box[x] = False
            for y in keys[x]:
                has_key[y] = True
                if has_box[y]:
                    dfs(y)
            for y in containedBoxes[x]:
                has_box[y] = True
                if has_key[y]:
                    dfs(y)
        for idx in initialBoxes:
            if has_box[idx] and has_key[idx]: dfs(idx)
        return res
# @lc code=end

