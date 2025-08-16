#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from typing import List
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = (1, 0), (0, 1), (-1, 0), (0, -1)
        m, n, wn = len(board), len(board[0]), len(word)
        def dfs(i, j, idx):
            if idx == wn: return True
            ch = board[i][j]
            board[i][j] = '#'
            for dx, dy in dir:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[idx]:
                    f = dfs(nx, ny, idx + 1)
                    if f: return True
            board[i][j] = ch
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1): return True
        return False
# @lc code=end

