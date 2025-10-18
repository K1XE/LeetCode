#
# @lc app=leetcode.cn id=3397 lang=python3
#
# [3397] 执行操作后不同元素的最大数量
#
from mytools import *
# @lc code=start
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        pre = -inf
        for x in nums:
            x = min(max(x - k, pre + 1), x + k)
            if x > pre:
                ans += 1
                pre = x
        return ans
# @lc code=end

