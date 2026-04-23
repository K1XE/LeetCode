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
            nonlocal pack
            if l + r == n << 1: res.append("".join(pack)); return
            if l > r and r < n: 
                pack.append(")")
                dfs(l, r + 1)
                pack.pop()
            if l < n:
                pack.append("(")
                dfs(l + 1, r)
                pack.pop()
        dfs(0, 0)
        return res
                
# @lc code=end

