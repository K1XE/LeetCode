#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from mytools import *
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)
        res = []
        b_ = [[] for _ in range(n + 1)]
        for k_, v in cnt.items():
            b_[v].append(k_)
        for i in range(n, -1, -1):
            res.extend(b_[i])
        while len(res) > k:
            res.pop()
        return res
# @lc code=end

