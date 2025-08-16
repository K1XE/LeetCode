#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#
from mytools import *
# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        x = list(str(num))
        for i in range(len(x)):
            if x[i] == '6': x[i] = '9'; break
        return int(''.join(x))

# @lc code=end

