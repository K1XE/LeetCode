#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: n = -n; x = 1 / x
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
# @lc code=end

