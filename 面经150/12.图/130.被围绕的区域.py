#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
from typing import List
# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir = (1, 0), (-1, 0), (0, 1), (0, -1)
        m, n = len(board), len(board[0])
        def dfs(x, y, s):
            board[x][y] = s
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == "O": dfs(nx, ny, s)
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == "O": dfs(i, j, "K")
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O": dfs(i, j, "X")
        for i in range(m):
            for j in range(n):
                if board[i][j] == "K": board[i][j] = "O"
# @lc code=end

