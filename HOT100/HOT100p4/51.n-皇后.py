#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from mytools import *
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        s = "." * n
        board = [list(s) for _ in range(n)]
        def ck(x, y):
            for i in range(n):
                if board[i][y] == "Q": return False
            for j in range(n):
                if board[x][j] == "Q": return False
            i, j = x, y
            while i >= 0 and j >= 0:
                if board[i][j] == "Q": return False
                i -= 1; j -= 1
            i, j = x, y
            while i >= 0 and j < n:
                if board[i][j] == "Q": return False
                i -= 1; j += 1
            return True
        res = []
        def dfs(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            for col in range(n):
                if ck(row, col):
                    board[row][col] = "Q"
                    dfs(row + 1)
                    board[row][col] = "."
        dfs(0)
        return res
# @lc code=end

