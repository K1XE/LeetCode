#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
from mytools import *
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        hash = defaultdict(list)
        n = len(beginWord)
        for w in wordList:
            for i in range(n):
                p = w[:i] + "*" + w[i + 1:]
                hash[p].append(w)
        bss = set([beginWord])
        ess = set([endWord])
        vis = set()
        step = 1
        while bss and ess:
            if len(bss) > len(ess):
                bss, ess = ess, bss
            nxt = set()
            for w in bss:
                for i in range(n):
                    p = w[:i] + "*" + w[i + 1:]
                    for tmp in hash[p]:
                        if tmp in ess: return step + 1
                        if tmp not in vis:
                            vis.add(tmp)
                            nxt.add(tmp)
            bss = nxt
            step += 1
        return 0
# @lc code=end

