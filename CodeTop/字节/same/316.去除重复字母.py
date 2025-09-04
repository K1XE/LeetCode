#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
from mytools import *
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        hash = Counter(s)
        stk = []
        for c in s:
            if c not in stk:
                while stk and c < stk[-1] and hash[stk[-1]] > 0: stk.pop()
                stk.append(c)
            hash[c] -= 1
        return ''.join(stk)
# @lc code=end

