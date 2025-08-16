#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from mytools import *
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pack = [["."] * n for _ in range(n)]
        res = []
        col = [0] * n
        diag1 = [0] * (2 * n)
        diag2 = [0] * (2 * n)
        def dfs(row):
            if row == n:
                res.append([''.join(rows) for rows in pack])
                return
            for col_ in range(n):
                if col[col_] or diag1[row + col_] or diag2[row - col_ + n]: continue
                col[col_] = diag1[row + col_] = diag2[row - col_ + n] = 1
                pack[row][col_] = 'Q'
                dfs(row + 1)
                pack[row][col_] = '.'
                col[col_] = diag1[row + col_] = diag2[row - col_ + n] = 0
        dfs(0)
        return res
# @lc code=end

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ss = "." * n
        pack = [ss for _ in range(n)]
        res = []
        def check(r, c):
            for i in range(n):
                if pack[i][c] == 'Q': return False
            for j in range(n):
                if pack[r][j] == 'Q': return False
            i, j = r, c
            while i >= 0 and j >= 0:
                if pack[i][j] == 'Q': return False
                i -= 1
                j -= 1
            i, j = r, c
            while i >= 0 and j < n:
                if pack[i][j] == 'Q': return False
                i -= 1
                j += 1
            return True
        def dfs(row):
            if row == n:
                res.append(pack[:])
                return
            for col_ in range(n):
                if check(row, col_):
                    pack[row] = pack[row][:col_] + 'Q' + pack[row][col_ + 1:]
                    dfs(row + 1)
                    pack[row] = pack[row][:col_] + '.' + pack[row][col_ + 1:]
        dfs(0)
        return res