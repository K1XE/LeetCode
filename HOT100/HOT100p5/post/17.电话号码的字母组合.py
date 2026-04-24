#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from mytools import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
            "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        n = len(digits)
        res = []
        pack = []
        def dfs(sta):
            nonlocal n
            if len(pack) == n:
                res.append("".join(pack))
                return
            for i in range(sta, n):
                for ch in h[digits[i]]:
                    pack.append(ch)
                    print(pack)
                    dfs(i + 1)
                    pack.pop()
        dfs(0)
        return res
# @lc code=end

