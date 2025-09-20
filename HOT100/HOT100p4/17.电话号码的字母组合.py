#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from mytools import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
                "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        n = len(digits)
        if n == 0: return []
        res = []
        pack = []
        def dfs(sta):
            nonlocal n
            if sta == n:
                if len(pack) == n: res.append(''.join(pack))
                return
            for i in range(sta, n):
                for ch in hash[digits[i]]:
                    pack.append(ch)
                    dfs(i + 1)
                    pack.pop()
        dfs(0)
        return res
# @lc code=end

