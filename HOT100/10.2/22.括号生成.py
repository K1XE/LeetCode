#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from mytools import *
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cnt1, cnt2 = 0, 0
        res= []
        pack = ""
        def dfs(cnt1, cnt2):
            nonlocal pack
            if cnt1 == cnt2 == n:
                res.append(pack)
                return
            if cnt1 < n:
                pack += "("
                dfs(cnt1 + 1, cnt2)
                pack = pack[:-1]
            if cnt2 < cnt1:
                pack += ")"
                dfs(cnt1, cnt2 + 1)
                pack = pack[:-1]
        dfs(0, 0)
        return res
# @lc code=end

