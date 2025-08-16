#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
from mytools import *
# @lc code=start
class Node:
    def __init__(self, end = False):
        self.end = end
        self.son = defaultdict(Node)
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for w in words:
            cur = root
            for ch in w: cur = cur.son[ch]
            cur.end = True
            cur.word = w
        res = set()
        m, n = len(board), len(board[0])
        dir = (1, 0), (-1, 0), (0, 1), (0, -1)
        def dfs(x: int, y: int, node: Node):
            ch = board[x][y]
            cur = node.son[ch]
            if cur.end: res.add(cur.word)
            board[x][y] = '#'
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    nxt = board[nx][ny]
                    if nxt in cur.son:
                        dfs(nx, ny, cur)
            board[x][y] = ch
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.son: dfs(i, j, root)
        return list(res)
# @lc code=end

