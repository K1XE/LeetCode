#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = []
        for ch in s:
            if (ch.isalnum()): ss.append(ch.lower())
        tmp = ''.join(ss)
        l, r = 0, len(tmp) - 1
        while l <= r:
            if tmp[l] != tmp[r]: return False
            l += 1; r -= 1
        return True
# @lc code=end

