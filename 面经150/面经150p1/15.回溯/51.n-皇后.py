#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        def check(x, y):
            for i in range(x + 1): 
                if board[i][y] == "Q": return False
            for j in range(y + 1):
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
        def dfs(r):
            if r == n:
                tmp = [''.join(row) for row in board]
                res.append(tmp.copy())
                return
            for col in range(n):
                if not check(r, col): continue
                board[r][col] = "Q"
                dfs(r + 1)
                board[r][col] = "."
        dfs(0)
        return res
# @lc code=end

