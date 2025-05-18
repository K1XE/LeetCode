from mytools import *
class Solution:
    
    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        d = ((0, 1), (0, -1), (1, 0), (-1, 0))
        dist[0][0] = 0
        hash = defaultdict(list)
        used = set()
        for i in range(m):
            for j in range(n):
                ch = matrix[i][j]
                if 'A' <= ch <= 'Z':
                    hash[ch].append((i, j))

        h = [(0, 0, 0)]
        heapq.heapify(h)
        while h:
            d0, x, y = heapq.heappop(h)
            if dist[x][y] < d0: continue
            if (x, y) == (m - 1, n - 1): return d0
            ch = matrix[x][y]
            if 'A' <= ch <= 'Z' and ch not in used:
                used.add(ch)
                for nx, ny in hash[ch]:
                    if (nx, ny) == (x, y): continue
                    if dist[nx][ny] > d0:
                        dist[nx][ny] = d0
                        heapq.heappush(h, (dist[nx][ny], nx, ny))
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    if dist[nx][ny] > d0 + 1:
                        dist[nx][ny] = d0 + 1
                        heapq.heappush(h, (dist[nx][ny], nx, ny))
        return -1


