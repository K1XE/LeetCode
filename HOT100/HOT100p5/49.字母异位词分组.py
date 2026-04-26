#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from mytools import *
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        for s in strs:
            h["".join(sorted([ch for ch in s]))].append(s)
        res = []
        for k, v in h.items():
            res.append(v)
        return res
        
# @lc code=end

