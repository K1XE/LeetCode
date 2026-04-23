#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from mytools import *
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        col_ = set()
        d1 = set()
        d2 = set()
        def ck(x, y):
            if y in col_ or (x - y) in d1 or (x + y) in d2: return False
            return True
        res = []
        def dfs(r):
            if r == n: res.append(["".join(s) for s in board.copy()]); return
            for col in range(n):
                if not ck(r, col): continue
                col_.add(col)
                d1.add(r - col)
                d2.add(r + col)
                board[r][col] = "Q"
                dfs(r + 1)
                board[r][col] = "."
                col_.remove(col)
                d1.remove(r - col)
                d2.remove(r + col)
        dfs(0)
        return res

# @lc code=end

