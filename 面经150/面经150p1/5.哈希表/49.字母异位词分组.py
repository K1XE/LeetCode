#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            hash[tuple(cnt)].append(s)
        return list(hash.values())
# @lc code=end

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            tmp = tuple(sorted(s))
            hash[tmp].append(s)
        res = []
        for _, l in hash.items():
            res.append(l)
        return res