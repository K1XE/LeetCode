#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from mytools import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = {}
        cur = 0
        eds = -inf
        res = []
        n = len(s)
        for i, x in enumerate(s): idx[x] = i
        for i in range(n):
            cur += 1
            eds = max(eds, idx[s[i]])
            if i >= eds: res.append(cur); cur = 0
        return res
# @lc code=end

