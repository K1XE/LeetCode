#
# @lc app=leetcode.cn id=966 lang=python3
#
# [966] 元音拼写检查器
#
from mytools import *
# @lc code=start
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        vow = "aeiou"
        def foo(s):
            return ''.join("*" if ch in vow else ch for ch in s.lower())
        wss = set(wordlist)
        lm = {}; vm = {}
        for s in wordlist:
            sl = s.lower()
            if sl not in lm: lm[sl] = s
            sv = foo(s)
            if sv not in vm: vm[sv] = s
        for q in queries:
            if q in wss: res.append(q)
            elif q.lower() in lm: res.append(lm[q.lower()])
            elif foo(q) in vm: res.append(vm[foo(q)])
            else: res.append("")
        return res
# @lc code=end

