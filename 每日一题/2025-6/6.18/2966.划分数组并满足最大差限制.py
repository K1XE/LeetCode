#
# @lc app=leetcode.cn id=2966 lang=python3
#
# [2966] 划分数组并满足最大差限制
#
from mytools import *
# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(0, n, 3):
            if (nums[i + 2] - nums[i] > k):
                res = []
                break
            res.append([nums[i], nums[i + 1], nums[i + 2]])
        return res
# @lc code=end

