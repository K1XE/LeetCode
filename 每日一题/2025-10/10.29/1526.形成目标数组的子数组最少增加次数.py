#
# @lc app=leetcode.cn id=1526 lang=python3
#
# [1526] 形成目标数组的子数组最少增加次数
#
from mytools import *
# @lc code=start
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        return target[0] + sum(max(y - x, 0) for x, y in pairwise(target))
    
# @lc code=end

