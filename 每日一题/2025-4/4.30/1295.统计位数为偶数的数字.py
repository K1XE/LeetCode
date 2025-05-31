#
# @lc app=leetcode.cn id=1295 lang=python3
#
# [1295] 统计位数为偶数的数字
#
from typing import List
# @lc code=start
class Solution:
    def solve(self, num) :
        res = 0
        while num :
            res += 1
            num //= 10
        return res
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)) :
            if (not (self.solve(nums[i]) % 2)) :
                res += 1
        return res



# @lc code=end

