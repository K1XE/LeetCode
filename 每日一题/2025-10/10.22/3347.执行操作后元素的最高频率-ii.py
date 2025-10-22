#
# @lc app=leetcode.cn id=3347 lang=python3
#
# [3347] 执行操作后元素的最高频率 II
#
from mytools import *
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1
        res = 0
        cur = 0
        for k_, v in sorted(diff.items()):
            cur += v
            res = max(res, min(cur, cnt[k_] + numOperations))
        return res
# @lc code=end

