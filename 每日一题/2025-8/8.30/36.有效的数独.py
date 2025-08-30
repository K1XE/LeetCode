#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from mytools import *
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_(x, y):
            for i in range(9):
                if i == x: continue
                if board[i][y] == board[x][y]: return False
            for j in range(9):
                if j == y: continue
                if board[x][j] == board[x][y]: return False
            bx, by = x // 3 * 3, y // 3 * 3
            for i in range(bx, bx + 3):
                for j in range(by, by + 3):
                    if i == x or j == y: continue
                    if board[i][j] == board[x][y]: return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." and not check_(i, j): return False
        return True
# @lc code=end

