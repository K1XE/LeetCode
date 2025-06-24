#
# @lc app=leetcode.cn id=2200 lang=python3
#
# [2200] 找出数组中的所有 K 近邻下标
#
from mytools import *
# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ss = set()
        n = len(nums)
        for i in range(n):
            if (nums[i] == key):
                ss.update(range(max(i - k, 0), min(i + k, n - 1) + 1))
        return list(ss)
# @lc code=end

