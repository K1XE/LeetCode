#
# @lc app=leetcode.cn id=2348 lang=python3
#
# [2348] 全 0 子数组的数目
#
from typing import List
# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        idx = 0
        while idx < n:
            tmp = 0
            cnt = 0
            while idx < n and nums[idx] == 0:
                cnt += 1
                tmp += cnt
                idx += 1
            idx += 1
            res += tmp
        return res
# @lc code=end

