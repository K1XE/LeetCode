#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
from mytools import *
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empty = []
        row_s = [set() for _ in range(9)]
        col_s = [set() for _ in range(9)]
        box_s = [set() for _ in range(9)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    row_s[i].add(board[i][j])
                    col_s[j].add(board[i][j])
                    box_idx = i // 3 * 3 + j // 3
                    box_s[box_idx].add(board[i][j])


        def dfs(pos):
            if (pos == len(empty)): return True
            x, y = empty[pos]
            bi = x // 3 * 3 + y // 3
            for i in range(1, 10):
                if str(i) in row_s[x] or str(i) in col_s[y] or str(i) in box_s[bi]: continue
                row_s[x].add(str(i))
                col_s[y].add(str(i))
                box_s[bi].add(str(i))
                board[x][y] = str(i)
                if dfs(pos + 1) : return True
                board[x][y] = '.'
                row_s[x].remove(str(i))
                col_s[y].remove(str(i))
                box_s[bi].remove(str(i))
            return False
        
        return dfs(0)



# @lc code=end

