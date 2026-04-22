#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from mytools import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = defaultdict(int)
        for i, x in enumerate(s):
            idx[x] = i
        n = len(s)
        cur = -inf
        res = []
        s_ = 0
        for i in range(n):
            cur = max(cur, idx[s[i]])
            if i == cur: res.append(i - s_ + 1); s_ += res[-1]
            
        return res
# @lc code=end

