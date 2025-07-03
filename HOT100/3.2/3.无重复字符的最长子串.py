#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from mytools import *
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = defaultdict(int)
        i = 0; n = len(s); res = 0
        for j in range(n):
            hash[s[j]] += 1
            while hash[s[j]] > 1:
                hash[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
# @lc code=end

