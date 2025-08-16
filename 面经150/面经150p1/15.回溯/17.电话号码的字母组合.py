#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from mytools import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        hash = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
                "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        res = []
        pack = []
        def dfs(sta):
            if sta == len(digits):
                res.append(''.join(pack))
                return
            for ch in hash[digits[sta]]:
                pack.append(ch)
                dfs(sta + 1)
                pack.pop()
        dfs(0)
        return res
# @lc code=end

