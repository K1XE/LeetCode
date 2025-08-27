#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from mytools import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = defaultdict(int)
        for i, ch in enumerate(s):
            hash[ch] = i
        n = len(s); i = 0
        res = []
        while i < n:
            eds = hash[s[i]]
            j = i + 1
            while j <= eds:
                eds = max(eds, hash[s[j]])
                j += 1
            res.append(j - i)
            i = j
        return res
# @lc code=end

