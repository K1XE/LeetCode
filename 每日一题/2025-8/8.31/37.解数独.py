#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
from typing import List
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        bs = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                bs[(i // 3) * 3 + j // 3].add(board[i][j])

        def dfs(pos):
            if pos == 81: return True
            tx, ty = pos // 9, pos % 9
            tb = (tx // 3) * 3 + ty // 3
            if board[tx][ty] != ".": return dfs(pos + 1)
            for x in map(str, range(1, 10)):
                if x not in rows[tx] and x not in cols[ty] and x not in bs[tb]:
                    board[tx][ty] = x
                    rows[tx].add(x); cols[ty].add(x); bs[tb].add(x)
                    if dfs(pos + 1): return True
                    board[tx][ty] = "."
                    rows[tx].remove(x); cols[ty].remove(x); bs[tb].remove(x)
            return False

        dfs(0)
        
# @lc code=end

