#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from mytools import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        hash = defaultdict(str)
        hash["2"] = "abc"
        hash["3"] = "def"
        hash["4"] = "ghi"
        hash["5"] = "jkl"
        hash["6"] = "mno"
        hash["7"] = "pqrs"
        hash["8"] = "tuv"
        hash["9"] = "wxyz"
        n = len(digits)
        res = []
        pack = ""
        def dfs(sta):
            nonlocal pack
            if sta == n:
                res.append(pack)
                return
            for ch in hash[digits[sta]]:
                pack += ch
                dfs(sta + 1)
                pack = pack[:-1]
        dfs(0)
        return res
# @lc code=end

