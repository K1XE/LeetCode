#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
from mytools import *
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        lastvis = 0
        for i in range(len(nums) - 1):
            curdiff = nums[i + 1] - nums[i]
            if (lastvis >= 0 and curdiff < 0) or (lastvis <= 0 and curdiff > 0):
                lastvis = curdiff
                res += 1
            elif curdiff != 0: lastvis = curdiff
        return res

# @lc code=end

