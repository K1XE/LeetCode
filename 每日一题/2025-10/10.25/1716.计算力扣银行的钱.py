#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#
from mytools import *
# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        D = 7
        w, r = divmod(n, D)
        return (w * D * (w + D) + r * (w * 2 + r + 1)) // 2

# @lc code=end

