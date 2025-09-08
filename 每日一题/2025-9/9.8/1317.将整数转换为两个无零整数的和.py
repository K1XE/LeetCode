#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#
from mytools import *
# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def ck(s):
            for ch in s: 
                if ch == "0": return False
            return True
        for i in range(1, n):
            s1 = str(i)
            s2 = str(n - i)
            if ck(s1) and ck(s2): return [i, n - i]
# @lc code=end

