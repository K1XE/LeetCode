#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        hash = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(n - 1):
            if hash[s[i]] < hash[s[i + 1]]:
                res -= hash[s[i]]
            else:
                res += hash[s[i]]
        return res + hash[s[-1]]
# @lc code=end

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        hash = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        i = 0
        while i + 1< n:
            if s[i] == 'I':
                if s[i + 1] == 'V':
                    res += 4
                    i += 2
                elif s[i + 1] == 'X':
                    res += 9
                    i += 2
                else:
                    res += 1
                    i += 1
            elif s[i] == 'X':
                if s[i + 1] == 'L':
                    res += 40
                    i += 2
                elif s[i + 1] == 'C':
                    res += 90
                    i += 2
                else:
                    res += 10
                    i += 1
            elif s[i] == 'C':
                if s[i + 1] == 'D':
                    res += 400
                    i += 2
                elif s[i + 1] == 'M':
                    res += 900
                    i += 2
                else:
                    res += 100
                    i += 1
            else:
                res += hash[s[i]]
                i += 1
        return res + hash[s[-1]] if i < n else res