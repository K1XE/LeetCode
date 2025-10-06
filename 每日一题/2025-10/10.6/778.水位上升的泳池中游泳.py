#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#
from mytools import *
# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = [(grid[0][0], 0, 0)]
        n = len(grid)
        dis = [[inf] * n for _ in range(n)]
        dis[0][0] = grid[0][0]
        while h:
            d, x, y = heappop(h)
            if x == y == n - 1: return d
            if d > dis[x][y]: continue
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < n and 0 <= ny < n:
                    curd = max(grid[nx][ny], d)
                    if curd < dis[nx][ny]:
                        dis[nx][ny] = curd
                        heappush(h, (curd, nx, ny))
        
# @lc code=end

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def ck(mx):
            vis = set()
            def dfs(x, y):
                if x == y == n - 1: return True
                vis.add((x, y))
                for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in vis and grid[nx][ny] <= mx and dfs(nx, ny): return True
                return False
            return dfs(0, 0)
        l = max(grid[0][0], grid[-1][-1]) - 1
        r = n ** 2 - 1
        while l + 1 < r:
            mid = l + r >> 1
            if ck(mid): r = mid
            else: l = mid
        return r 