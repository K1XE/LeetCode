#
# @lc app=leetcode.cn id=3170 lang=python3
#
# [3170] 删除星号以后字典序最小的字符串
#
from mytools import *
# @lc code=start
class Solution:
    def clearStars(self, s: str) -> str:
        stk =[]
        pos = defaultdict(list)
        for c in s:
            if c != "*":
                stk.append(c)
                pos[c].append(len(stk) - 1)
            else:
                for i in range(26):
                    ch = chr(ord('a') + i)
                    if pos[ch]:
                        p = pos[ch].pop()
                        stk[p] = ''
                        break
        return ''.join(stk)
# @lc code=end

