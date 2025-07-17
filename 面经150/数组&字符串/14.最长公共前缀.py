#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from mytools import *
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = inf
        sn = len(strs)
        for s in strs:
            n = min(n, len(s))
        for i in range(n):
            for j in range(1, sn):
                if i >= len(strs[j]) or strs[j][i] != strs[j - 1][i]: return strs[j][0:i]
        return strs[0][:n]
# @lc code=end

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch: return strs[0][:i]
        return strs[0]