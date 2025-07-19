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
        can = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                can[i] = can[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                can[i] = max(can[i + 1] + 1, can[i])
        return sum(can)
# @lc code=end

