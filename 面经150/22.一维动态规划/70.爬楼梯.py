#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(n + 1):
            if i >= 2:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
# @lc code=end

