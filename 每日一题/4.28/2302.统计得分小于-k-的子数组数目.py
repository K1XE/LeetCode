#
# @lc app=leetcode.cn id=2302 lang=python3
#
# [2302] 统计得分小于 K 的子数组数目
#
from typing import List
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        res = 0
        sums = 0
        for j in range(len(nums)) :
            sums += nums[j]
            while sums * (j - i + 1) >= k :
                sums -= nums[i]
                i += 1
            res += j - i + 1
        return res
# @lc code=end

