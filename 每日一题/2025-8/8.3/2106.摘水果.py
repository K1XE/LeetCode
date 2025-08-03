#
# @lc app=leetcode.cn id=2106 lang=python3
#
# [2106] 摘水果
#
from mytools import *
# @lc code=start
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        l = bisect_left(fruits, [startPos - k])
        r = bisect_left(fruits, [startPos + 1])
        res = s = sum(f[1] for f in fruits[l:r])
        while r < len(fruits) and fruits[r][0] - startPos <= k:
            s += fruits[r][1]
            while fruits[r][0] * 2 - fruits[l][0] - startPos > k and \
                fruits[r][0] - fruits[l][0] * 2 + startPos > k:
                s -= fruits[l][1]
                l += 1
            res = max(res, s)
            r += 1
        return res
# @lc code=end

