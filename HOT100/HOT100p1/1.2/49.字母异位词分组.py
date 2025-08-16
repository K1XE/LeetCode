#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from mytools import *
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            ss = tuple(sorted(s))
            hash[ss].append(s)
        return list(hash.values())
# @lc code=end

