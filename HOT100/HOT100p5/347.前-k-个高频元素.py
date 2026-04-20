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
        b_ = [[] for _ in range(n + 1)]
        for k_, v in cnt.items():
            b_[v].append(k_)
        res = []
        for i in range(n, - 1, - 1):
            if b_[i]: res.extend(b_[i])
        while len(res) > k:
            res.pop()
        return res
# @lc code=end
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1
        res = []
        for k_, v in cnt.items():
            if len(res) == k: heappushpop(res, (v, k_))
            else: heappush(res, (v, k_))
        return [x for _, x in res]
