#
# @lc app=leetcode.cn id=3370 lang=python3
#
# [3370] 仅含置位位的最小整数
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        n |= (1 << n.bit_length()) - 1
        return n
# @lc code=end

