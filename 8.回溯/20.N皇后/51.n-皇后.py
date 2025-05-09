#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from mytools import *
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()
        res = []
        pack = ['.' * n for _ in range(n)]
        def dfs(row, res: List, pack: List):
            if row == n:
                res.append(pack[:])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2: continue
                pack[row] = pack[row][:col] + 'Q' + pack[row][col + 1:]
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                row += 1
                dfs(row, res, pack)
                row -= 1
                pack[row] = pack[row][:col] + '.' + pack[row][col + 1:]
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        dfs(0, res, pack)
        return res
# @lc code=end

