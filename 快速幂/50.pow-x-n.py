#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            n = -n
            x = 1/x
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans
# @lc code=end

