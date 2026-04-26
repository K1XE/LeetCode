#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
from mytools import *
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        h[0] = 1
        res = 0
        s = 0
        for i, x in enumerate(nums):
            s += x
            res += h[s - k]
            
            h[s] += 1

        return res
# @lc code=end

