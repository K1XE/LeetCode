#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from mytools import *
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = (1, 0), (0, 1), (-1, 0), (0, -1)
        lw = len(word)
        m, n = len(board), len(board[0])
        def dfs(i, j, idx):
            if idx == lw:
                return True
            tmp = board[i][j]
            board[i][j] = "#"
            for dx, dy in d:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[idx]:
                    f = dfs(nx, ny, idx + 1)
                    if f: return True
            board[i][j] = tmp
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1): return True
        return False
# @lc code=end

