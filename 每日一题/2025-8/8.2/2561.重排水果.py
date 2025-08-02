#
# @lc app=leetcode.cn id=2561 lang=python3
#
# [2561] 重排水果
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        hash = defaultdict(int)
        for x, y in zip(basket1, basket2):
            hash[x] += 1
            hash[y] -= 1
        a = []; b = []
        for x, cnt in hash.items():
            if cnt & 1 == 1: return -1
            if cnt > 0: a.extend([x] * (cnt // 2))
            else: b.extend([x] * (-cnt // 2))
        a.sort(); b.sort(reverse=True)
        min_ = min(hash)
        return sum(min(u, v, 2 * min_) for u, v in zip(a, b))
# @lc code=end

