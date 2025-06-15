#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from mytools import *
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_ = defaultdict(int)
        for x in nums:
            hash_[x] += 1
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        for k_, v in hash_.items():
            bucket[v].append(k_)
        res = []
        for i in range(n, -1, -1):
            if bucket[i] != 0: res.extend(bucket[i])
        while len(res) > k:
            res.pop()
        return res
# @lc code=end

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_ = defaultdict(int)
        for x in nums:
            hash_[x] += 1
        h = []
        for k_, v in hash_.items():
            if len(h) < k: heapq.heappush(h, (v, k_))
            else: heapq.heappushpop(h, (v, k_))
        res = []
        for v, k_ in h:
            res.append(k_)
        return res