#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from mytools import *
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False
        _n = len(word)
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(board), len(board[0])
        vis = [[False] * n for _ in range(m)]
        def dfs(x, y, cur):
            if board[x][y] != word[cur]: return False
            if cur == _n - 1:
                return board[x][y] == word[cur]
            vis[x][y] = True
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                    cur += 1
                    res = dfs(nx, ny, cur)
                    if res: return True
                    cur -= 1
                    
            vis[x][y] = False
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False


# @lc code=end

