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
            tmp = [0] * 26
            for ch in s: tmp[ord(ch) - ord('a')] += 1
            ts = ''.join(str(tmp))
            hash[ts].append(s)
        return [v for _, v in hash.items()]
# @lc code=end

