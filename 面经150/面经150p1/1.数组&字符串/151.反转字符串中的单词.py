#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return ' '.join(reversed(words))
# @lc code=end

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1
        s = list(s)
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        idx1 = 0
        idx2 = n - 1
        while idx1 < n and s[idx1] == ' ': idx1 += 1
        while idx2 >= 0 and s[idx2] == ' ': idx2 -= 1
        t = 0
        while idx1 <= idx2:
            while idx1 <= idx2 and s[idx1] == ' ': idx1 += 1
            left = l = idx1
            while idx1 <= idx2 and s[idx1] != ' ': idx1 += 1
            right = r = idx1 - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1; r -= 1
            while left <= right:
                s[t] = s[left]
                t += 1; left += 1
            if t < n: s[t] = ' '; t += 1
        return ''.join(s[:t]) if s[t - 1] != ' ' else ''.join(s[:t - 1])