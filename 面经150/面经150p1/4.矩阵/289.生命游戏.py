#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
from typing import List

'''pre = 0 post = 1 : 2
   pre = 1 post = 0 : 3
   pre = 0 post = 0 : 4
   pre = 1 post = 1 : 5'''
# @lc code=start

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(i, j):
            cnt = 0
            for k in range(max(0, i - 1), min(i + 2, m)):
                for u in range(max(0, j - 1), min(j + 2, n)):
                    if k == i and u == j: continue
                    x = board[k][u]
                    if x == 1 or x == 3 or x == 5: cnt += 1
            return cnt
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt = check(i, j)
                if cnt < 2 or cnt > 3:
                    if board[i][j] == 0: board[i][j] = 4
                    elif board[i][j] == 1: board[i][j] = 3
                elif cnt == 2:
                    if board[i][j] == 0: board[i][j] = 4
                    elif board[i][j] == 1: board[i][j] = 5
                elif cnt == 3:
                    if board[i][j] == 0: board[i][j] = 2
                    elif board[i][j] == 1: board[i][j] = 5
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2 or board[i][j] == 5: board[i][j] = 1
                else: board[i][j] = 0
# @lc code=end

