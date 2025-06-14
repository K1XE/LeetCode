#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from mytools import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c : i for i, c in enumerate(s)}
        sta = eds = 0
        res = []
        for i, c in enumerate(s):
            eds = max(eds, last[c])
            if i == eds:
                res.append(eds - sta + 1)
                sta = eds + 1
        return res
# @lc code=end

