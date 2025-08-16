#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
from mytools import *
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        hash = defaultdict(int)
        hash[0] = 1
        sums_ = 0
        for i in range(n):
            sums_ += nums[i]
            if sums_ - k in hash:
                res += hash[sums_ - k]
            hash[sums_] += 1
        return res
# @lc code=end

