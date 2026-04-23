#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from mytools import *
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word)
        d = (1, 0), (-1, 0), (0, 1), (0, -1)
        def dfs(x, y, idx):
            if idx >= l - 1: return True
            tmp = board[x][y]
            board[x][y] = "#"
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[idx + 1]:
                    if dfs(nx, ny, idx + 1):
                        return True
            board[x][y] = tmp
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0): return True
        return False
# @lc code=end

