#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from mytools import *
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = (0, 1), (0, -1), (1, 0), (-1, 0)
        m, n = len(board), len(board[0])
        l = len(word)
        def dfs(x, y, idx):
            nonlocal m, n, l
            if idx >= l - 1: return True
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and word[idx + 1] == board[nx][ny]:
                    tmp = board[nx][ny]
                    board[nx][ny] = "#"
                    if dfs(nx, ny, idx + 1): return True
                    board[nx][ny] = tmp
            return False
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = "#"
                    if dfs(i, j, 0): return True
                    board[i][j] = tmp
        return False
# @lc code=end

