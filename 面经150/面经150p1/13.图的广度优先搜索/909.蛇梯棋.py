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
            row = n - (pos - 1) // n - 1
            tmp = pos - n * (n - row - 1)
            col = (tmp - 1) if (n - row) % 2 == 1 else (n - tmp)
            return row, col
        q = deque()
        q.append((1, 0))
        vis = set([1])
        while q:
            cur, step = q.popleft()
            if cur == n * n: return step
            for mov in range(1, 7):
                nxt = cur + mov
                if nxt > n * n: break
                row, col = get_rc(nxt)
                if board[row][col] != -1:
                    nxt = board[row][col]
                if nxt not in vis: q.append((nxt, step + 1)); vis.add(nxt)
        return -1

# @lc code=end

