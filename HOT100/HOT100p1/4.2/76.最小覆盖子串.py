#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from mytools import *
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = defaultdict(int)
        for ch in t: hash[ch] += 1
        i = 0
        n = len(s)
        need = len(hash)
        valid = 0
        sta = 0
        minl = inf
        for j in range(n):
            if s[j] in hash:
                hash[s[j]] -= 1
                if hash[s[j]] == 0: valid += 1
            while i <= j and valid == need:
                if j - i + 1 < minl:
                    sta = i
                    minl = j - i + 1
                if s[i] in hash:
                    hash[s[i]] += 1
                    if hash[s[i]] > 0: valid -= 1
                i += 1
        return s[sta:sta + minl] if minl != inf else ""
# @lc code=end

