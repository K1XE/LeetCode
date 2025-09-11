#
# @lc app=leetcode.cn id=2785 lang=python3
#
# [2785] 将字符串中的元音字母排序
#
from mytools import * 
# @lc code=start
class Solution:
    def sortVowels(self, s: str) -> str:
        hash = defaultdict(int)
        ss = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        a = list(s)
        cur = []
        for i, ch in enumerate(s):
            if ch in ss: cur.append(ch)
        cur.sort()
        idx = 0
        for i, ch in enumerate(s):
            if ch in ss: a[i] = cur[idx]; idx += 1
        return ''.join(a)
# @lc code=end

