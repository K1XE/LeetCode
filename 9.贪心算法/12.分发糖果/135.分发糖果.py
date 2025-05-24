#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
from mytools import *
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1: return 1
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i + 1] + 1, res[i])
        return sum(res)
# @lc code=end

