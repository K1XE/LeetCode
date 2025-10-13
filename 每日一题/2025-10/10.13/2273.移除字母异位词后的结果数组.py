#
# @lc app=leetcode.cn id=2273 lang=python3
#
# [2273] 移除字母异位词后的结果数组
#
from mytools import *
# @lc code=start
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        d = [False] * n
        cnt = Counter(words[0])
        for i, w in enumerate(words[1:]):
            cnt1 = Counter(w)
            if cnt1 == cnt: d[i + 1] = True
            else: cnt = cnt1
        res = []
        for i, w in enumerate(words):
            if not d[i]: res.append(w)
        return res
# @lc code=end

