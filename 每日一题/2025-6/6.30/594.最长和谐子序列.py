#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#
from mytools import *
# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        sta = 0
        res = 0
        for i in range(1, n):
            while sta <= i and nums[i] - nums[sta] > 1:
                sta += 1
            if nums[i] - nums[sta] == 1:
                res = max(res, i - sta + 1)
        return res
# @lc code=end

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for x in cnt:
            if x + 1 in cnt:
                res = max(res, cnt[x] + cnt[x + 1])
        return res