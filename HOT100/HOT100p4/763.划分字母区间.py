#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from mytools import *
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        laxt = defaultdict(int)
        for i, ch in enumerate(s): laxt[ch] = i
        n = len(s)
        i = 0
        res = []
        sta = 0
        while i < n:
            eds = laxt[s[i]]
            sta = i
            j = i + 1
            while j < n and j < eds:
                if laxt[s[j]] > eds: eds = laxt[s[j]]
                j += 1
            res.append(eds - sta + 1)
            i = eds + 1
        return res
# @lc code=end

