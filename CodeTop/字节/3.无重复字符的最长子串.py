#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = defaultdict(int)
        j = 0
        res = 0
        for i in range(len(s)):
            hash[s[i]] += 1
            while hash[s[i]] > 1:
                hash[s[j]] -= 1
                j += 1
            res = max(i -j + 1, res)
        return res
# @lc code=end

