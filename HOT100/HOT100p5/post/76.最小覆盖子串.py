#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from mytools import *
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h = defaultdict(int)
        for i in range(len(t)):
            h[t[i]] += 1
        need = len(h)
        res = ""
        j = 0
        for i in range(len(s)):
            if s[i] in h:
                h[s[i]] -= 1
                if h[s[i]] == 0: need -= 1
            while need == 0:
                if i - j + 1 < len(res) or not res:
                    res = s[j:i + 1]
                if s[j] in h:
                    h[s[j]] += 1
                    if h[s[j]] > 0: need += 1
                j += 1
        return res
            
# @lc code=end

