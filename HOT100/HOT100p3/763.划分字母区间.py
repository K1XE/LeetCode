#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        laxt = defaultdict(int)
        for i, ch in enumerate(s):
            laxt[ch] = i
        idx = 0; n = len(s)
        res = []
        while idx < n:
            eds = laxt[s[idx]]
            j = idx
            while j < eds:
                if laxt[s[j]] > eds:
                    eds = laxt[s[j]]
                j += 1
            res.append(eds - idx + 1)
            idx = eds + 1
        return res
# @lc code=end

