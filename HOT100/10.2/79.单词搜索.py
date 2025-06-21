#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from mytools import *
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = (1, 0), (-1, 0), (0, 1), (0, -1)
        m, n = len(board), len(board[0])
        wn = len(word)
        vis = [[False] * n for _ in range(m)]
        def dfs(x, y, cnt):
            vis[x][y] = True
            if cnt == wn: return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and board[nx][ny] == word[cnt]:
                    if dfs(nx, ny, cnt + 1): return True
            vis[x][y] = False
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1): return True
        return False
# @lc code=end

