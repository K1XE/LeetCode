#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from mytools import *
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for x in nums:
            hash[x] += 1
        h = []
        for key, val in hash.items():
            heapq.heappush(h, (val, key))
            if len(h) > k: heapq.heappop(h)

        return [x for _, x in h]

# @lc code=end

