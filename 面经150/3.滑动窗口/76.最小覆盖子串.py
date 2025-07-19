#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from mytools import *
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = Counter(t)
        n = len(s); j = 0
        valid = 0
        sta = -1; l = inf
        for i in range(n):
            if s[i] in hash:
                hash[s[i]] -= 1
                if hash[s[i]] == 0: valid += 1
            while valid == len(hash):
                if i - j + 1 < l:
                    l = i - j + 1
                    sta = j
                if s[j] in hash:
                    hash[s[j]] += 1
                    if hash[s[j]] > 0: valid -= 1
                j += 1
        return s[sta: sta + l] if l != inf else ""
# @lc code=end

