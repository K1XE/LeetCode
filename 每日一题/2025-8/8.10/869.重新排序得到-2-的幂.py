#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#
from mytools import *
# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        hash = {''.join(sorted(str(1 << i))) for i in range(30)}
        s = ''.join(sorted(str(n)))
        return s in hash
# @lc code=end

