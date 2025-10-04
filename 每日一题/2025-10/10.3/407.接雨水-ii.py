#
# @lc app=leetcode.cn id=407 lang=python3
#
# [407] 接雨水 II
#
from mytools import *
# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        h = []
        m, n = len(heightMap), len(heightMap[0])
        for i, row in enumerate(heightMap):
            for j, hi in enumerate(row):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    h.append((hi, i, j))
                    row[j] = -1
        heapify(h)
        res = 0
        while h:
            cur, i, j = heappop(h)
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] != -1:
                    res += max(cur - heightMap[x][y], 0)
                    heappush(h, (max(cur, heightMap[x][y]), x, y))
                    heightMap[x][y] = -1
        return res
# @lc code=end

