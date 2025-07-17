#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
# @lc code=end
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i] != ' ': break
        res = 0
        print(i)
        while i >= 0 and s[i] != ' ':
            res += 1
            i -= 1
        return res
