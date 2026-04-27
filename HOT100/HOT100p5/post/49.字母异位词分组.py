#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from mytools import *
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idx = [0] * 26
        h = defaultdict(list)
        for s in strs:
            for ch in s:
                idx[ord(ch) - ord("a")] += 1
            
            h[str(idx)].append(s)
            idx = [0] * 26
        print("".join(str(idx)))
        return [v for _,v in h.items()]
# @lc code=end

