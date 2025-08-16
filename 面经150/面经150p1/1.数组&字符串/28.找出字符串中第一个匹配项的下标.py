#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
from mytools import *
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_nxt(s: str):
            j = 0
            n = len(s)
            nxt = [0] * n
            for i in range(1, n):
                while j > 0 and s[i] != s[j]: j = nxt[j - 1]
                if s[i] == s[j]: j += 1
                nxt[i] = j
            return nxt
        nxt = get_nxt(needle)
        j = 0
        n = len(haystack)
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]: j = nxt[j - 1]
            if haystack[i] == needle[j]: j += 1
            if j == len(needle): return i - len(needle) + 1
        return -1
# @lc code=end

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_nxt(s: str):
            n = len(s)
            nxt = [-1] * n
            j = -1
            for i in range(1, n):
                while j >= 0 and s[i] != s[j + 1]: j = nxt[j]
                if s[i] == s[j + 1]: j += 1
                nxt[i] = j
            return nxt
        nxt = get_nxt(needle)
        j = -1
        n = len(haystack)
        for i in range(n):
            while j >= 0 and haystack[i] != needle[j + 1]:
                j = nxt[j]
            if haystack[i] == needle[j + 1]: j += 1
            if j == len(needle) - 1: return i - len(needle) + 1
        return -1