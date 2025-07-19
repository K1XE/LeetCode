#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
from mytools import *
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            if c >= n: cnt[n] += 1
            else: cnt[c] += 1
        sums_= 0
        for i in range(n, - 1, - 1):
            sums_ += cnt[i]
            if sums_ >= i: return i
        return 0
# @lc code=end

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hash = defaultdict(int)
        for c in citations:
            for x in range(1, c + 1): hash[x] += 1
        n = len(citations)
        res = 0
        for i in range(1, n + 1):
            if hash[i] >= i:
                res = i
        return res