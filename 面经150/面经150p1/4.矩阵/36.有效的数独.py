#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
from typing import List
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            ss = set()
            for j in range(n):
                if board[i][j] == ".": continue
                x = int(board[i][j]) 
                if x in ss: return False
                ss.add(x)
        for i in range(n):
            ss = set()
            for j in range(n):
                if board[j][i] == ".": continue
                x = int(board[j][i]) 
                if x in ss: return False
                ss.add(x)
        for i in range(3):
            for j in range(3):
                ss = set()
                for k in range(3 * i, 3 * (i + 1)):
                    for u in range(3 * j, 3 * (j + 1)):
                        if board[k][u] == ".": continue
                        x = int(board[k][u])
                        if x in ss: return False
                        ss.add(x)
        return True
# @lc code=end

