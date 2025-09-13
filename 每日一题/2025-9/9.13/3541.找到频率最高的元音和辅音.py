#
# @lc app=leetcode.cn id=3541 lang=python3
#
# [3541] 找到频率最高的元音和辅音
#
from mytools import *
# @lc code=start
class Solution:
    def maxFreqSum(self, s: str) -> int:
        hash1 = [0] * 26
        hash2 = [0] * 26
        max1 = max2 = 0
        for ch in s:
            if ch in "aeiou":
                hash1[ord(ch) - ord('a')] += 1
                if hash1[ord(ch) - ord('a')] > max1:
                    max1 = hash1[ord(ch) - ord('a')]
            else:
                hash2[ord(ch) - ord('a')] += 1
                if hash2[ord(ch) - ord('a')] > max2:
                    max2 = hash2[ord(ch) - ord('a')]
        return max1 + max2
                
# @lc code=end

