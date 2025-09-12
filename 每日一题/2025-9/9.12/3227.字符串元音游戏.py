#
# @lc app=leetcode.cn id=3227 lang=python3
#
# [3227] 字符串元音游戏
#
from mytools import *
# @lc code=start
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(ch in "aeiou" for ch in s)
# @lc code=end

