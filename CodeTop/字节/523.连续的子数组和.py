#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
from mytools import *
# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n + 1): s[i] = s[i - 1] + nums[i - 1]
        ss = set()
        for i in range(2, n + 1):
            ss.add(s[i - 2] % k)
            if s[i] % k in ss: return True
        return False
            
# @lc code=end

