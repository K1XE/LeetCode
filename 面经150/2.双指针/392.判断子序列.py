#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        sn, tn = len(s), len(t)
        while i < sn and j < tn:
            if s[i] == t[j]:
                i += 1; j += 1
            elif s[i] != t[j]:
                j += 1
        return i == sn
# @lc code=end

