#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
from collections import defaultdict
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
# @lc code=end
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n1 = len(s); n2 = len(t)
        if n1 != n2: return False
        s2t = defaultdict(str)
        t2s = defaultdict(str)
        for i in range(n1):
            if s[i] in s2t and s2t[s[i]] != t[i]: return False
            if t[i] in t2s and t2s[t[i]] != s[i]: return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
