#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
from mytools import *
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_next(s: str, next: List):
            n = len(s)
            j = 0
            next[0] = 0
            for i in range(1, n):
                while j > 0 and s[i] != s[j]: j = next[j - 1]
                if s[i] == s[j]: j += 1
                next[i] = j
            return next
        n = len(needle)
        next = [0] * n
        next = get_next(needle, next)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n: return i - j
            else:
                if j > 0: j = next[j - 1]
                else: i += 1
        return -1

# @lc code=end

