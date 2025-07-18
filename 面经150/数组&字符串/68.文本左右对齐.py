#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from mytools import *
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        idx = 0
        while idx < n:
            l = idx
            s = 0
            while idx < n and s + len(words[idx]) + idx - l <= maxWidth:
                s += len(words[idx])
                idx += 1
            r = idx - 1
            num_words = r - l + 1
            total_space = maxWidth - s
            line = ""
            if idx == n or num_words == 1:
                line = ' '.join(words[l:idx])
                line += ' ' * (maxWidth - len(line))
            else:
                space = total_space // (num_words - 1)
                ex = total_space % (num_words - 1)
                for i in range(l, r):
                    line += words[i]
                    line += ' ' * (space + (1 if i - l < ex else 0))
                line += words[r]
            res.append(line)
        return res
# @lc code=end

