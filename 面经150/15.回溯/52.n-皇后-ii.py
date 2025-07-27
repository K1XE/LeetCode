#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = ["." * n for _ in range(n)]
        res = 0
        def check(x, y):
            for i in range(x):
                if board[i][y] == "Q": return False
            for j in range(y):
                if board[x][j] == "Q": return False
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q": return False
                i -= 1; j -= 1
            i, j = x - 1, y + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q": return False
                i -= 1; j += 1
            return True
        def dfs(r):
            if r == n:
                nonlocal res
                res += 1
                return
            for c in range(n):
                if not check(r, c): continue
                board[r] = board[r][:c] + "Q" + board[r][c + 1:]
                dfs(r + 1)
                board[r] = board[r][:c] + "." + board[r][c + 1:]
        dfs(0)
        return res
# @lc code=end

