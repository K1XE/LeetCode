#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from mytools import *
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        h = Counter(p)
        need = len(h)
        j = 0
        res = []
        for i in range(len(s)):
            if s[i] in h:
                h[s[i]] -= 1
                if h[s[i]] == 0: need -= 1
            while need == 0:
                if i - j + 1 == len(p):
                    res.append(j)
                if s[j] in h:
                    h[s[j]] += 1
                    if h[s[j]] > 0: need += 1
                j += 1
        return res
# @lc code=end

