#
# @lc app=leetcode.cn id=3085 lang=python3
#
# [3085] 成为 K 特殊字符串需要删除的最少字符数
#
from mytools import *
# @lc code=start
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        res = inf
        for t in range(max(freq) + 1):
            tmp = 0
            for f in freq:
                if f < t:
                    tmp += f
                elif f > t + k:
                    tmp += f - (t + k)
            res = min(res, tmp)
        return res
# @lc code=end

