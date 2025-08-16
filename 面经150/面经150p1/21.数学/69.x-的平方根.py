#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2 + 1
        while l <= r:
            mid = l + r >> 1
            if mid * mid > x: r = mid - 1
            elif mid * mid < x: l = mid + 1
            else: return mid
        return r

# @lc code=end

