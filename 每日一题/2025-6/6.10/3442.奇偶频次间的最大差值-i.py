#
# @lc app=leetcode.cn id=3442 lang=python3
#
# [3442] 奇偶频次间的最大差值 I
#
from mytools import *
# @lc code=start
class Solution:
    def maxDifference(self, s: str) -> int:
        hash = defaultdict(int)
        for ch in s:
            hash[ch] += 1
        maxa1 = 0
        mina2 = float('inf')
        for k, v in hash.items():
            if v % 2 and v > maxa1:
                maxa1 = v
            if not v % 2 and v < mina2:
                mina2 = v
        return maxa1 - mina2
# @lc code=end

