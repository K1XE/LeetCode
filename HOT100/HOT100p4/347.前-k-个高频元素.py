#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
from mytools import *
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = Counter(nums)
        res = []
        n = len(nums)
        b = [[] for _ in range(n + 1)]
        for k_, v in hash.items():
            b[v].append(k_)
            
# @lc code=end

