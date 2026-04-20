#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from mytools import *
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 1
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cur = nums[i]
                    cnt = 1
        return cur
# @lc code=end

