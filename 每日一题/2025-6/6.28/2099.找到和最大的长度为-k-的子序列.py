#
# @lc app=leetcode.cn id=2099 lang=python3
#
# [2099] 找到和最大的长度为 K 的子序列
#
from mytools import *
# @lc code=start
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        h = heapq.nlargest(k, enumerate(nums), key=lambda x: x[1])
        h.sort(key=lambda x: x[0])
        return [x[1] for x in h]
# @lc code=end

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i, x in enumerate(nums):
            heapq.heappush(h, (x, i))
            if len(h) > k: heapq.heappop(h)
        h.sort(key=lambda x: x[1])
        return [x for x, _ in h]