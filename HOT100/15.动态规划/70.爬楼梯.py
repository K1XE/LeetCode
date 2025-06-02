#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        a1, a2 = 1, 0
        b1, b2 = 1, 0
        for i in range(2, n + 1):
            c1 = b1 + b2
            c2 = a1 + a2
            a1, a2, b1, b2 = b1, b2, c1, c2
        return b1 + b2
            

# @lc code=end
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [[0] * 3 for _ in range(n + 1)]
        f[1][1] = 1
        f[0][1] = 1
        if n <= 2: return n
        for i in range(2, n + 1):
            f[i][1] = f[i - 1][1] + f[i - 1][2]
            f[i][2] = f[i - 2][1] + f[i - 2][2]
        return f[n][1] + f[n][2]
            

