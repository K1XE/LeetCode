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
        row_used = [[0] * 10 for _ in range(9)]
        col_used = [[0] * 10 for _ in range(9)]
        box_used = [[0] * 10 for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row_used[i][num] = 1
                    col_used[j][num] = 1
                    box_used[i // 3 * 3 + j // 3][num] = 1
                else: empty.append((i, j))
        # def check(row, col, x ,board):
        #     for i in range(9):
        #         if board[i][col] == str(x): return False
        #     for i in range(9):
        #         if board[row][i] == str(x): return False
        #     mrow = row // 3 * 3
        #     mcol = col // 3 * 3
        #     for i in range(mrow, mrow + 3):
        #         for j in range(mcol, mcol + 3):
        #             if board[i][j] == str(x): return False
        #     return True
        
        def dfs(pos):
            if pos == len(empty): return True
            row, col = empty[pos]
            box_idx = row // 3 * 3 + col // 3
            for x in range(1, 10):
                if not row_used[row][x]\
                    and not col_used[col][x]\
                        and not box_used[box_idx][x]:
                    board[row][col] = str(x)
                    row_used[row][x] = col_used[col][x] = box_used[box_idx][x] = 1
                    if dfs(pos + 1): return True
                    board[row][col] = '.'
                    row_used[row][x] = col_used[col][x] = box_used[box_idx][x] = 0
            return False

        return dfs(0)

# @lc code=end

