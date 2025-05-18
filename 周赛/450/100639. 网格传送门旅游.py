from mytools import *
class Solution:
    
    def minMoves(self, matrix: List[str]) -> int:
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        q = deque()
        q.append((0, 0))
        INT = 10**18
        dist = [[INT] * n for _ in range(m)]
        dist[0][0] = 0
        step = 0
        hash = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if 'A' <= matrix[i][j] <= 'Z':
                    hash[matrix[i][j]].append((i, j))
        used = set()
        while q:
            x, y = q.popleft()
            d0 = dist[x][y]
            if x == m - 1 and y == n - 1: return d0
            ch = matrix[x][y]
            if 'A' <= ch <= 'Z' and ch not in used:
                used.add(ch)
                for nx, ny in hash[ch]:
                    if (nx, ny) == (x, y): continue
                    if dist[nx][ny] > d0:
                        dist[nx][ny] = d0
                        q.appendleft((nx, ny))
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    if dist[nx][ny] > d0 + 1:
                        dist[nx][ny] = d0 + 1
                        q.append((nx, ny))  
        return -1
