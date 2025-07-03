#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from mytools import *
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash = defaultdict(int)
        for ch in p: hash[ch] += 1
        i = 0
        n = len(s)
        need = len(hash)
        valid = 0
        res = []
        for j in range(n):
            if s[j] in hash:
                hash[s[j]] -= 1
                if hash[s[j]] == 0:
                    valid += 1
            while valid == need:
                if j - i + 1 == len(p): res.append(i)
                if s[i] in hash:
                    hash[s[i]] += 1
                    if hash[s[i]] > 0: valid -= 1
                i += 1
        return res
# @lc code=end

