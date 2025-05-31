#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
from mytools import *
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [[1, 0], [-1 ,0], [0, 1], [0, -1]]
        m, n = len(board), len(board[0])
        def dfs(x, y):
            board[x][y] = 'K'
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    dfs(nx, ny)
        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n - 1] == 'O': dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m - 1][j] == 'O': dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O': board[i][j] = 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'K': board[i][j] = 'O'
                
            
# @lc code=end

