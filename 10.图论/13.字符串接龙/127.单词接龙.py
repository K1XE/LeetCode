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
        ss = set()
        vis = defaultdict(int)
        for s in wordList:
            ss.add(s)
        vis[beginWord] = 1
        q = deque()
        q.append(beginWord)
        while q:
            ww = q.popleft()
            stps = vis[ww]
            for i in range(len(ww)):
                ww_ = list(ww)
                for j in range(26):
                    ww_[i] = chr(j + ord('a'))
                    newww_ = ''.join(ww_)
                    if newww_ == endWord: return stps + 1
                    if newww_ in ss and newww_ not in vis:
                        vis[newww_] = stps + 1
                        q.append(newww_)
        return 0
# @lc code=end

