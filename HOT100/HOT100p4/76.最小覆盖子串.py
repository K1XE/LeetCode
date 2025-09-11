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
        need = len(hash)
        valid = 0
        j = 0
        eds = inf; sta = -inf
        for i, ch in enumerate(s):
            if ch in hash:
                hash[ch] -= 1
                if hash[ch] == 0: valid += 1
            while valid == need:
                if i - j < eds - sta: eds = i; sta = j
                if s[j] in hash:
                    hash[s[j]] += 1
                    if hash[s[j]] > 0: valid -= 1
                j += 1
        return s[sta:eds + 1] if sta != -inf else ""

# @lc code=end

