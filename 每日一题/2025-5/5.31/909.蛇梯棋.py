#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#
from mytools import *
# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_rc(pos):
            row = n - 1 - (pos - 1) // n
            col = (pos - 1) % n
            if (n - 1 - row) % 2 == 1:
                col = n - 1 - col
            return row, col
        vis = set()
        q = deque()
        q.append((1, 0))
        while q:
            cur, step = q.popleft()
            if cur == n * n: return step
            for move in range(1, 7):
                nxt_pos = cur + move
                if nxt_pos > n * n: break
                row, col = get_rc(nxt_pos)
                if board[row][col] != -1:
                    nxt_pos = board[row][col]
                if nxt_pos not in vis:
                    vis.add(nxt_pos)
                    q.append((nxt_pos, step + 1))
        return -1
        
# @lc code=end

