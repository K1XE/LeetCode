#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
from mytools import *
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash = defaultdict(str)
        hash["2"] = "abc"
        hash["3"] = "def"
        hash["4"] = "ghi"
        hash["5"] = "jkl"
        hash["6"] = "mno"
        hash["7"] = "pqrs"
        hash["8"] = "tuv"
        hash["9"] = "wxyz"
        def dfs(res: List, pack: List, idx):
            if idx == len(digits):
                res.append("".join(pack))
                return
            for ch in hash[digits[idx]]:
                pack.append(ch)
                idx += 1
                dfs(res, pack, idx)
                idx -= 1
                pack.pop()
        res = []
        if not digits: return res
        dfs(res, [], 0)
        return res

# @lc code=end

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash = defaultdict(str)
        hash["2"] = "abc"
        hash["3"] = "def"
        hash["4"] = "ghi"
        hash["5"] = "jkl"
        hash["6"] = "mno"
        hash["7"] = "pqrs"
        hash["8"] = "tuv"
        hash["9"] = "wxyz"
        def dfs(res: List, s: str, stai):
            if len(s) == len(digits):
                res.append(s)
                return
            for i in range(stai, len(digits)):
                for j in range(0, len(hash[digits[i]])):
                    s += hash[digits[i]][j]
                    dfs(res, s, i + 1)
                    s = s[:-1]
        res = []
        if not digits: return res
        dfs(res, "", 0)
        return res