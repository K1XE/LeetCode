#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from mytools import *
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = j = 0
        res = 0
        cur = 0
        for i in range(n):
            if nums[i] == 0: k -= 1
            while k < 0:
                if nums[j] == 0: k += 1
                j += 1
            cur = i - j + 1
            res = max(res, cur)
        return res
                
            
# @lc code=end
