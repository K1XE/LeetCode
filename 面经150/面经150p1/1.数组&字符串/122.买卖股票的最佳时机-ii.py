#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from mytools import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        no = 0
        have = -prices[0]
        for p in prices: no, have = max(no, have + p), max(have, no - p)
        return no
# @lc code=end

