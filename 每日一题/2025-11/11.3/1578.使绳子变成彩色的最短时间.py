#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 使绳子变成彩色的最短时间
#
from mytools import*
# @lc code=start
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = max_t = 0
        for i, t in enumerate(neededTime):
            res += t
            if t > max_t: max_t = t
            if i == len(neededTime) - 1 or colors[i] != colors[i + 1]:
                res -= max_t
                max_t = 0
        return res
# @lc code=end

