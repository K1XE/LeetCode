#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from mytools import *
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        pack = []
        def dfs(l, r):
            nonlocal n
            if l == r == n:
                res.append(''.join(pack))
                return
            if l < n:
                pack.append("(")
                dfs(l + 1, r)
                pack.pop()
            if r < l:
                pack.append(")")
                dfs(l, r + 1)
                pack.pop()
        dfs(0, 0)
        return res
# @lc code=end

