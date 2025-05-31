#
# @lc app=leetcode.cn id=2962 lang=python3
#
# [2962] 统计最大元素出现至少 K 次的子数组
#
from typing import List
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxval = max(nums)
        res = 0
        i = 0
        cnt = 0
        for j in range(len(nums)) :
            if nums[j] == maxval : cnt += 1
            while cnt >= k :
                res += len(nums) - j
                if nums[i] == maxval : cnt -= 1
                i += 1
        return res
# @lc code=end

