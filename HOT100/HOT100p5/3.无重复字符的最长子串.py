#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from mytools import *
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = defaultdict(int)
        j = 0
        res = 0
        n = len(s)
        for i in range(n):
            h[s[i]] += 1
            while h[s[i]] > 1:
                h[s[j]] -= 1
                j += 1
            print(i, j)
            res = max(res, i - j + 1)
        
        return res
            
# @lc code=end

