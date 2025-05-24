#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#
from mytools import *
# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        h = nums
        heapq.heapify(h)
        for _ in range(k):
            tmp = heapq.heappop(h)
            heapq.heappush(h, -tmp)
        return sum(h)
# @lc code=end

