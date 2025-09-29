#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from mytools import *
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash = Counter(p)
        valid = 0
        need = len(hash)
        n = len(s)
        j = 0
        res = []
        for i in range(n):
            if s[i] in hash:
                hash[s[i]] -= 1
                if hash[s[i]] == 0: valid += 1
            while valid == need:
                if i - j + 1 == len(p): res.append(j)
                if s[j] in hash:
                    hash[s[j]] += 1
                    if hash[s[j]] > 0: valid -= 1
                j += 1
        return res
# @lc code=end

