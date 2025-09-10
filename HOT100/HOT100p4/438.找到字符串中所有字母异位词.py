#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
from mytools import *
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        need = len(cnt)
        n = len(s)
        valid = 0
        res = []
        j = 0
        for i in range(n):
            if s[i] in cnt:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0: valid += 1
            while valid == need:
                if i - j + 1 == len(p): res.append(j)
                if s[j] in cnt:
                    cnt[s[j]] += 1
                    if cnt[s[j]] > 0: valid -= 1
                j += 1
        return res
# @lc code=end

