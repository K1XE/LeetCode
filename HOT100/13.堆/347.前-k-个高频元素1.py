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
        max_cnt = 0
        for x in nums:
            hash[x] += 1
            max_cnt = max(max_cnt, hash[x])
        bucket = [[] for _ in range(max_cnt + 1)]
        for key, val in hash.items():
            bucket[val].append(key)
        res = []
        for i in range(max_cnt, -1, -1):
            if bucket[i]:
                for x in bucket[i]:
                    res.append(x)
            k -= len(bucket[i])
            if k <= 0: break
        return res
            
# @lc code=end

