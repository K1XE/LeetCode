#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from mytools import *
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        tmp = ""
        for i in range(n):
            tmp += "."
        board = [tmp for _ in range(n)]
        res = []
        def check(row, col):
            for i in range(0, row + 1):
                if board[i][col] == 'Q': return False
            for j in range(0, col + 1):
                if board[row][j] == 'Q': return False
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q': return False
                i -= 1
                j -= 1
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q': return False
                i -= 1
                j += 1
            return True
        def dfs(row):
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                if check(row, col):
                    board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                    dfs(row + 1)
                    board[row] = board[row][:col] + '.' + board[row][col + 1:]
        dfs(0)
        return res
# @lc code=end

