#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#
from mytools import *
# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        sn = list(str(n))
        flag = len(sn)
        for i in range(len(sn) - 1, 0, -1):
            if sn[i] < sn[i - 1]:
                flag = i
                sn[i - 1] = str(int(sn[i - 1]) - 1)
        for i in range(flag, len(sn)):
            sn[i] = '9'
        return int(''.join(sn))
# @lc code=end

