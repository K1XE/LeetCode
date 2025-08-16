#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res
# @lc code=end

class Solution:
    def reverseBits(self, n: int) -> int:
        p = 2 ** 30
        q = 2 ** 1
        res = 0
        while n:
            if n // p >= 1: n %= p; res += q
            p /= 2; q *= 2
        return res