#
# @lc app=leetcode.cn id=3289 lang=python3
#
# [3289] 数字小镇中的捣蛋鬼
#
from mytools import *
# @lc code=start
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [x for x, v in Counter(nums).items() if v == 2]
# @lc code=end

