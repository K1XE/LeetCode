from mytools import *
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        lcnt = 0
        sx = sy = 0
        m, n = len(classroom), len(classroom[0])
        idx = [[0] * n for _ in range(m)]
        for i, row in enumerate(classroom):
            for j, ch in enumerate(row):
                if ch == 'S':
                    sx, sy = i, j
                if ch == 'L':
                    idx[i][j] = ~(1 << lcnt)
                    lcnt += 1
        if lcnt == 0: return 0
        fmask = (1 << lcnt) - 1
        d = (0, 1), (0, -1), (-1, 0), (1, 0)
        vis = [[[[False] * (1 << lcnt) for _ in range(energy + 1)] for _ in range(n)] for _ in range(m)]
        vis[sx][sy][energy][fmask] = True
        res = 0
        q = [(sx, sy, energy, fmask)]
        while q:
            tmp = q
            q = []
            for x, y, e, mask in tmp:
                if mask == 0: return res
                if e == 0: continue
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <=ny < n and classroom[nx][ny] != 'X':
                        e_ = energy if classroom[nx][ny] == 'R' else e - 1
                        mask_ = mask & idx[nx][ny] if classroom[nx][ny] == 'L' else mask
                        if not vis[nx][ny][e_][mask_]:
                            vis[nx][ny][e_][mask_] = True
                            q.append((nx, ny, e_, mask_))
            res += 1
        return -1