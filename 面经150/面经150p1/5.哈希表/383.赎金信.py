#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
from mytools import *
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = Counter(magazine)
        for ch in ransomNote:
            hash[ch] -= 1
            if hash[ch] < 0: return False
        return True
# @lc code=end

