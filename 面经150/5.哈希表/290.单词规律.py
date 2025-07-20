#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
from collections import defaultdict
# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        hash1, hash2 = {}, {}
        for p, w in zip(pattern, words):
            if hash1.get(w, p) != p or hash2.get(p, w) != w:
                return False
            hash1[w] = p
            hash2[p] = w
        return True
# @lc code=end

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tmp = s.split()
        n1 = len(pattern); n2 = len(tmp)
        if n1 != n2: return False
        hash1 = defaultdict(str)
        hash2 = defaultdict(str)
        for i in range(n1):
            if pattern[i] not in hash1:
                hash1[pattern[i]] = tmp[i]
            else:
                if tmp[i] != hash1[pattern[i]]: return False
            if tmp[i] not in hash2:
                hash2[tmp[i]] = pattern[i]
            else:
                if pattern[i] != hash2[tmp[i]]: return False
        return True