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
        r = set()
        d1 = set()
        d2 = set()
        res = []
        def dfs(row):
            if row == n:
                res.append(["".join(s) for s in board])
            for c in range(n):
                if c not in r and c - row not in d1 and c + row not in d2:
                    r.add(c)
                    d1.add(c - row)
                    d2.add(c + row)
                    board[row][c] = "Q"
                    dfs(row + 1)
                    board[row][c] = "."
                    r.remove(c)
                    d1.remove(c - row)
                    d2.remove(c + row)
        dfs(0)
        return res

# @lc code=end

